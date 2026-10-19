"""Plan or execute resumable, date-partitioned LSE reference-table exports.

Default behavior builds a local SQLite queue only. Executing a batch requires
--execute plus an explicit phrase, hidden API-key entry, a fresh /usage check,
and leaves a safety reserve under weekly/monthly byte quotas. The official SDK
dataset() export endpoint is used; no live stream is opened.

This can create many paid/limited provider jobs. Review the plan and terms before
execution. Each artifact remains private LSE-derived data.
"""

from __future__ import annotations

import argparse
import getpass
import json
import sqlite3
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote


def parse_day(value: Any) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def chunks(start: date, end: date, unit: str):
    cursor = start
    while cursor <= end:
        if unit == "day":
            stop = cursor
        elif unit == "month":
            if cursor.month == 12:
                next_month = date(cursor.year + 1, 1, 1)
            else:
                next_month = date(cursor.year, cursor.month + 1, 1)
            stop = min(end, next_month - timedelta(days=1))
        else:
            stop = min(end, date(cursor.year, 12, 31))
        yield cursor, stop
        cursor = stop + timedelta(days=1)


def partition_unit(name: str, row_count: int, start: date | None, end: date | None) -> str:
    if name in {"options_flow", "options_flow_1m"}:
        return "day"
    if name == "options_chain":
        return "month"
    if start and end and row_count > 1_000_000 and (end - start).days < 550:
        return "month"
    return "year"


def make_plan(refs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    tasks = []
    for ref in refs:
        name = str(ref.get("dataset") or "")
        if not name:
            continue
        count = int(ref.get("rows") or 0)
        first, last = parse_day(ref.get("first")), parse_day(ref.get("last"))
        if first and last:
            unit = partition_unit(name, count, first, last)
            periods = list(chunks(first, last, unit))
            total_days = max(1, (last - first).days + 1)
            for start, end in periods:
                span = (end - start).days + 1
                estimate = round(count * span / total_days)
                tasks.append({
                    "dataset": name, "start": start.isoformat(), "end": end.isoformat(),
                    "partition_unit": unit, "provider_total_rows_metadata": count,
                    "estimated_rows_only": estimate,
                    "status": "pending",
                })
        else:
            tasks.append({
                "dataset": name, "start": None, "end": None,
                "partition_unit": "snapshot", "provider_total_rows_metadata": count,
                "estimated_rows_only": count, "status": "pending",
            })
    return tasks


def init_db(db: sqlite3.Connection) -> None:
    db.execute("""CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY,
        dataset TEXT NOT NULL,
        start_date TEXT,
        end_date TEXT,
        partition_unit TEXT NOT NULL,
        row_estimate INTEGER,
        status TEXT NOT NULL DEFAULT 'pending',
        output_path TEXT,
        output_bytes INTEGER,
        error_status INTEGER,
        updated_at_utc TEXT
    )""")
    db.commit()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("preflight_json", type=Path)
    parser.add_argument("--out", type=Path, default=Path("lse_reference_exports"))
    parser.add_argument("--execute", action="store_true", help="run a quota-limited export batch")
    parser.add_argument("--max-jobs", type=int, default=1, help="jobs in this invocation; default one")
    parser.add_argument("--reserve-mib-month", type=int, default=1024)
    parser.add_argument("--reserve-mib-week", type=int, default=512)
    args = parser.parse_args()
    if not args.preflight_json.is_file():
        print("Preflight JSON not found; no request made.", file=sys.stderr)
        return 2
    preflight = json.loads(args.preflight_json.read_text(encoding="utf-8"))
    refs = preflight.get("metadata", {}).get("reference_inventory", [])
    if not refs:
        print("Preflight contains no reference_inventory; no request made.", file=sys.stderr)
        return 2

    args.out.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(args.out / "reference_export_manifest.sqlite")
    init_db(db)
    existing = db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    if not existing:
        for task in make_plan(refs):
            db.execute("INSERT INTO tasks(dataset,start_date,end_date,partition_unit,row_estimate,status) VALUES(?,?,?,?,?,'pending')",
                       (task["dataset"], task["start"], task["end"], task["partition_unit"], task["estimated_rows_only"]))
        db.commit()

    summary = db.execute("SELECT partition_unit,status,COUNT(*) FROM tasks GROUP BY partition_unit,status ORDER BY partition_unit,status").fetchall()
    total = db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    print(f"Reference inventory datasets: {len(refs)}; planned partitions: {total}")
    for unit, status, count in summary:
        print(f"  {unit:8} {status:10} {count:,}")
    print("Provider row counts are estimates only; partition sizes and date semantics must be verified.")
    if not args.execute:
        print(f"Plan-only mode. Manifest: {(args.out / 'reference_export_manifest.sqlite').resolve()}")
        db.close()
        return 0
    if args.max_jobs < 1:
        print("--max-jobs must be positive.", file=sys.stderr)
        db.close()
        return 2
    if input("Type EXPORT REFERENCE PARTITIONS to continue: ").strip() != "EXPORT REFERENCE PARTITIONS":
        print("Cancelled; no key requested and no export job started.")
        db.close()
        return 0
    try:
        from lse import LSE
    except ImportError:
        print("Missing SDK. Install with: python -m pip install lse-data", file=sys.stderr)
        db.close()
        return 2
    key = getpass.getpass("LSE API key (input hidden): ").strip()
    if not key:
        print("No key entered; no export started.", file=sys.stderr)
        db.close()
        return 2
    try:
        client = LSE(api_key=key)
    except Exception as exc:
        key = ""
        print(f"Client initialization failed ({type(exc).__name__}); details suppressed.", file=sys.stderr)
        db.close()
        return 1
    key = ""

    try:
        usage = client._vault_call("/usage")
    except Exception as exc:
        print(f"Fresh usage check failed ({type(exc).__name__}, status={getattr(exc, 'status', None)}); no export started.", file=sys.stderr)
        db.close()
        return 1
    print("Fresh account usage:", json.dumps(usage, sort_keys=True))
    jobs_remaining = int(usage.get("exports_cap_hour") or 0) - int(usage.get("exports_this_hour") or 0)
    if jobs_remaining <= 0:
        print("No export job allowance remains this hour; no export started.")
        db.close()
        return 1
    run_jobs = min(args.max_jobs, jobs_remaining)
    month_cap, week_cap = int(usage.get("bytes_cap_month") or 0), int(usage.get("bytes_cap_week") or 0)
    month_used, week_used = int(usage.get("bytes_used_month") or 0), int(usage.get("bytes_used_week") or 0)
    if ((month_cap and month_cap - month_used <= max(0, args.reserve_mib_month) * 1024 * 1024) or
            (week_cap and week_cap - week_used <= max(0, args.reserve_mib_week) * 1024 * 1024)):
        print("Configured byte safety reserve would be breached; no export started.")
        db.close()
        return 1

    completed = 0
    while completed < run_jobs:
        # Start with the smallest inventory-estimated partitions to learn actual
        # Parquet sizes before attempting the very large options-flow partitions.
        task = db.execute("SELECT task_id,dataset,start_date,end_date,partition_unit,row_estimate FROM tasks WHERE status='pending' ORDER BY row_estimate ASC,task_id ASC LIMIT 1").fetchone()
        if not task:
            break
        task_id, dataset, start, end, unit, estimate = task
        part_name = f"{start or 'all'}_{end or 'all'}"
        dest = args.out / dataset / part_name
        try:
            path = client.dataset(dataset, start=start, end=end, dest=str(dest), dataframe=False)
            size = Path(path).stat().st_size
            db.execute("UPDATE tasks SET status='complete',output_path=?,output_bytes=?,updated_at_utc=? WHERE task_id=?",
                       (str(path), size, datetime.now(timezone.utc).isoformat(timespec="seconds"), task_id))
            db.commit()
            completed += 1
            print(f"Completed export {completed}/{run_jobs}: {dataset} {start or 'all'}..{end or 'all'} rows_estimate={estimate} bytes={size}")
        except Exception as exc:
            status = getattr(exc, "status", None)
            db.execute("UPDATE tasks SET status='blocked',error_status=?,updated_at_utc=? WHERE task_id=?",
                       (status if isinstance(status, int) else None,
                        datetime.now(timezone.utc).isoformat(timespec="seconds"), task_id))
            db.commit()
            print(f"Export stopped at {dataset} {start or 'all'}..{end or 'all'} ({type(exc).__name__}, status={status}); details suppressed.")
            break
        try:
            usage = client._vault_call("/usage")
        except Exception as exc:
            print(f"Post-export usage check failed ({type(exc).__name__}); stopping before next job.")
            break
        month_used, week_used = int(usage.get("bytes_used_month") or 0), int(usage.get("bytes_used_week") or 0)
        if ((month_cap and month_cap - month_used <= max(0, args.reserve_mib_month) * 1024 * 1024) or
                (week_cap and week_cap - week_used <= max(0, args.reserve_mib_week) * 1024 * 1024)):
            print("Stopping at configured byte safety reserve.")
            break
    pending = db.execute("SELECT COUNT(*) FROM tasks WHERE status='pending'").fetchone()[0]
    blocked = db.execute("SELECT COUNT(*) FROM tasks WHERE status='blocked'").fetchone()[0]
    db.close()
    print(f"Batch ended: completed={completed}; pending={pending:,}; blocked={blocked:,}.")
    print("Re-run on later hours to resume; review licenses, returned file sizes, and partition coverage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
