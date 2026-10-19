"""Resumable downloader for cataloged 1d candles and series (no raw ticks).

The default mode creates/updates a SQLite task manifest and prints scope only.
To execute a bounded batch, pass --execute; the script then requests explicit
confirmation, prompts for the key invisibly, and issues at most --max-calls
bounded synchronous REST calls. It never calls history(), dataset(), or stream().

All response partitions are private local LSE data. Keep them outside the vault
and do not redistribute. Check terms and current account usage before execution.
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


def as_date(value: Any) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def date_next(value: Any) -> date | None:
    parsed = as_date(value)
    return parsed + timedelta(days=1) if parsed else None


def json_line(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)


def database_init(db: sqlite3.Connection) -> None:
    db.execute("""CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY,
        kind TEXT NOT NULL,
        dataset TEXT NOT NULL,
        symbol TEXT NOT NULL,
        start_date TEXT,
        end_date TEXT,
        status TEXT NOT NULL DEFAULT 'pending',
        next_start TEXT,
        row_count INTEGER NOT NULL DEFAULT 0,
        page_count INTEGER NOT NULL DEFAULT 0,
        error_status INTEGER,
        updated_at_utc TEXT
    )""")
    db.execute("""CREATE TABLE IF NOT EXISTS pages (
        task_id INTEGER NOT NULL,
        page_no INTEGER NOT NULL,
        start_date TEXT,
        end_date TEXT,
        row_count INTEGER NOT NULL,
        byte_count INTEGER NOT NULL,
        first_time TEXT,
        last_time TEXT,
        file_path TEXT NOT NULL,
        PRIMARY KEY(task_id, page_no)
    )""")
    # Older versions of this helper may have created duplicate task keys before
    # an explicit unique index was added. Keep the oldest checkpoint per key.
    duplicate_ids = [row[0] for row in db.execute(
        "SELECT task_id FROM tasks WHERE task_id NOT IN "
        "(SELECT MIN(task_id) FROM tasks GROUP BY kind,dataset,symbol)"
    ).fetchall()]
    if duplicate_ids:
        db.executemany("DELETE FROM pages WHERE task_id=?", [(task_id,) for task_id in duplicate_ids])
        db.executemany("DELETE FROM tasks WHERE task_id=?", [(task_id,) for task_id in duplicate_ids])
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS tasks_unique_source ON tasks(kind,dataset,symbol)")
    db.commit()


def initialize_tasks(db: sqlite3.Connection, catalog: list[dict[str, Any]], meta: dict[str, Any], snapshot_date: date) -> int:
    before = int(db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0])
    candle_classes = list(dict.fromkeys(meta.get("candle_classes", []) + meta.get("synth_candle_classes", [])))
    series_classes = set(meta.get("series_classes", []))
    created = 0
    for row in catalog:
        dataset, symbol = row.get("dataset"), row.get("symbol")
        if not dataset or not symbol:
            continue
        kind = "candles_1d" if dataset in candle_classes else "series" if dataset in series_classes else None
        if not kind:
            continue
        start = as_date(row.get("first"))
        end = as_date(row.get("last"))
        if not start:
            start = end
        if not end or end > snapshot_date:
            end = snapshot_date
        if start and start > end:
            # A future-dated first/last pair cannot be pulled as past observations.
            continue
        db.execute(
            "INSERT OR IGNORE INTO tasks(kind,dataset,symbol,start_date,end_date,status,next_start,updated_at_utc) VALUES(?,?,?,?,?,'pending',?,?)",
            (kind, dataset, symbol, start.isoformat() if start else None,
             end.isoformat() if end else None, start.isoformat() if start else None,
             datetime.now(timezone.utc).isoformat(timespec="seconds")),
        )
        created += 1
    db.commit()
    after = int(db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0])
    return after - before


def output_partition(root: Path, kind: str, dataset: str, symbol: str, page_no: int) -> Path:
    safe_symbol = quote(symbol, safe="")
    return root / kind / dataset / safe_symbol / f"part-{page_no:05d}.jsonl"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog_json", type=Path)
    parser.add_argument("preflight_json", type=Path)
    parser.add_argument("--out", type=Path, default=Path("lse_daily_series"))
    parser.add_argument("--max-calls", type=int, default=40, help="maximum data requests this run; default 40")
    parser.add_argument("--pause-seconds", type=float, default=0.4, help="pacing between requests")
    parser.add_argument("--usage-check-every", type=int, default=500,
                        help="poll /usage every N successful data calls; 0 disables periodic checks")
    parser.add_argument("--limit", type=int, default=5000, help="rows per request; max 5000")
    parser.add_argument("--reserve-mib-month", type=int, default=1024,
                        help="stop before leaving less than this much monthly byte quota")
    parser.add_argument("--reserve-mib-week", type=int, default=512,
                        help="stop before leaving less than this much weekly byte quota")
    parser.add_argument("--retry-blocked", action="store_true",
                        help="requeue blocked tasks with transient HTTP status 0/408/429/500/502/503/504")
    parser.add_argument("--execute", action="store_true", help="make bounded REST calls; default is manifest-only")
    args = parser.parse_args()
    args.limit = max(1, min(args.limit, 5000))
    if not args.catalog_json.is_file() or not args.preflight_json.is_file():
        print("Catalog/preflight file missing; no request made.", file=sys.stderr)
        return 2
    catalog_payload = json.loads(args.catalog_json.read_text(encoding="utf-8"))
    preflight = json.loads(args.preflight_json.read_text(encoding="utf-8"))
    catalog = catalog_payload.get("catalog", [])
    meta = preflight.get("metadata", {}).get("vault_meta", {})
    usage = preflight.get("metadata", {}).get("usage", {})
    snapshot_dt = as_date(catalog_payload.get("retrieved_at_utc")) or datetime.now(timezone.utc).date()
    args.out.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(args.out / "acquisition_manifest.sqlite")
    database_init(db)
    if args.retry_blocked:
        requeued = db.execute(
            "UPDATE tasks SET status='pending',error_status=NULL,updated_at_utc=? "
            "WHERE status='blocked' AND error_status IN (0,408,429,500,502,503,504)",
            (datetime.now(timezone.utc).isoformat(timespec="seconds"),),
        ).rowcount
        db.commit()
        if requeued:
            print(f"Requeued {requeued} blocked transient task(s) for retry.")
    before = db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    count = initialize_tasks(db, catalog, meta, snapshot_dt)
    totals = db.execute("SELECT kind,status,COUNT(*) FROM tasks GROUP BY kind,status ORDER BY kind,status").fetchall()
    print(f"Catalog snapshot rows: {len(catalog):,}; persisted daily/series tasks: {count:,}; prior tasks: {before:,}")
    print("Tasks by type/status:")
    for kind, status, n in totals:
        print(f"  {kind:12} {status:10} {n:,}")
    print("Preflight usage snapshot:", json.dumps(usage, sort_keys=True))
    print(f"Per-run call cap: {args.max_calls}; per-request row cap: {args.limit}; pause: {args.pause_seconds}s")
    print(f"Private output root: {args.out.resolve()}")
    if not args.execute:
        print("Preview only. No API key requested and no data calls made. Add --execute to run a bounded batch.")
        db.close()
        return 0
    if args.max_calls < 1:
        print("--max-calls must be positive.", file=sys.stderr)
        db.close()
        return 2
    if input("Type FETCH DAILY/SERIES to start this bounded batch: ").strip() != "FETCH DAILY/SERIES":
        print("Cancelled; no API key requested and no data calls made.")
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
        print("No key entered; no data call made.", file=sys.stderr)
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

    def usage_snapshot() -> dict[str, Any] | None:
        for attempt in range(3):
            try:
                return client._vault_call("/usage")
            except Exception as exc:
                status = getattr(exc, "status", None)
                if status == 429 and attempt < 2:
                    delay = 5 * (2 ** attempt)
                    print(f"Usage endpoint rate-limited (429); retrying in {delay}s ({attempt + 1}/2).")
                    time.sleep(delay)
                    continue
                print(f"Usage check failed ({type(exc).__name__}, status={status}); stopping before next data batch.")
                return None
        return None

    usage_now = usage_snapshot()
    if usage_now is None:
        db.close()
        return 1
    month_cap = int(usage_now.get("bytes_cap_month") or 0)
    week_cap = int(usage_now.get("bytes_cap_week") or 0)
    month_reserve = max(0, args.reserve_mib_month) * 1024 * 1024
    week_reserve = max(0, args.reserve_mib_week) * 1024 * 1024
    print("Fresh usage before data requests:", json.dumps(usage_now, sort_keys=True))
    if ((month_cap and month_cap - int(usage_now.get("bytes_used_month") or 0) <= month_reserve) or
            (week_cap and week_cap - int(usage_now.get("bytes_used_week") or 0) <= week_reserve)):
        print("Configured safety reserve would be breached; no data request made.")
        db.close()
        return 1

    request_count = 0
    pause = max(0.35, args.pause_seconds)
    while request_count < args.max_calls:
        task = db.execute(
            "SELECT task_id,kind,dataset,symbol,start_date,end_date,next_start,page_count,row_count FROM tasks WHERE status IN ('pending','partial') ORDER BY task_id LIMIT 1"
        ).fetchone()
        if not task:
            break
        task_id, kind, dataset, symbol, start_date, end_date, next_start, page_no, total_rows = task
        if not next_start:
            next_start = start_date
        if not next_start or not end_date:
            db.execute("UPDATE tasks SET status='needs_review',updated_at_utc=? WHERE task_id=?",
                       (datetime.now(timezone.utc).isoformat(timespec="seconds"), task_id))
            db.commit()
            continue
        request_error = None
        rows = None
        time_field = "timestamp" if kind == "candles_1d" else "date"
        for attempt in range(3):
            try:
                if kind == "candles_1d":
                    rows = client.candles(symbol, timeframe="1d", start=next_start, end=end_date,
                                          limit=args.limit, order="asc", dataset=dataset)
                else:
                    rows = client.series(symbol, dataset=dataset, start=next_start, end=end_date,
                                         limit=args.limit, order="asc")
                request_error = None
                break
            except Exception as exc:
                request_error = exc
                status = getattr(exc, "status", None)
                if status not in (0, 408, 429, 500, 502, 503, 504) or attempt == 2:
                    break
                delay = 2 ** (attempt + 1)
                print(f"Transient endpoint failure for {dataset}/{symbol} (status={status}); retrying in {delay}s ({attempt + 1}/2).")
                time.sleep(delay)
        if request_error is not None:
            status = getattr(request_error, "status", None)
            # Preserve resumability and suppress exception body/headers.
            db.execute("UPDATE tasks SET status='blocked',error_status=?,updated_at_utc=? WHERE task_id=?",
                       (status if isinstance(status, int) else None,
                        datetime.now(timezone.utc).isoformat(timespec="seconds"), task_id))
            db.commit()
            print(f"Stopped at {kind} {dataset}/{symbol}; request failed ({type(request_error).__name__}, status={status}).")
            break

        rows = rows if isinstance(rows, list) else []
        page_path = output_partition(args.out, kind, dataset, symbol, int(page_no))
        page_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = page_path.with_suffix(page_path.suffix + ".tmp")
        wrapped = [
            {"source": "LSE", "dataset": dataset, "symbol": symbol,
             "resolution": "1d" if kind == "candles_1d" else "native_series",
             "request_start": next_start, "request_end": end_date,
             "catalog_snapshot": args.catalog_json.name,
             "retrieved_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
             "row": row}
            for row in rows
        ]
        encoded = "".join(json_line(r) + "\n" for r in wrapped)
        tmp_path.write_text(encoded, encoding="utf-8")
        tmp_path.replace(page_path)
        page_bytes = page_path.stat().st_size
        first_time = rows[0].get(time_field) if rows else None
        last_time = rows[-1].get(time_field) if rows else None
        new_total = int(total_rows) + len(rows)
        full_page = len(rows) >= args.limit
        next_cursor = date_next(last_time) if full_page and last_time else None
        status_new = "partial" if next_cursor and next_cursor.isoformat() <= end_date else "complete"
        if status_new == "complete":
            next_cursor = None
        db.execute("INSERT OR REPLACE INTO pages VALUES(?,?,?,?,?,?,?,?,?)",
                   (task_id, page_no, next_start, end_date, len(rows), page_bytes,
                    str(first_time) if first_time is not None else None,
                    str(last_time) if last_time is not None else None, str(page_path)))
        db.execute("UPDATE tasks SET status=?,next_start=?,row_count=?,page_count=?,error_status=NULL,updated_at_utc=? WHERE task_id=?",
                   (status_new, next_cursor.isoformat() if next_cursor else None, new_total,
                    page_no + 1, datetime.now(timezone.utc).isoformat(timespec="seconds"), task_id))
        db.commit()
        request_count += 1
        print(f"[{request_count}/{args.max_calls}] {status_new}: {kind} {dataset}/{symbol} start={next_start} rows={len(rows)} total={new_total}")
        if args.usage_check_every > 0 and request_count % args.usage_check_every == 0:
            usage_now = usage_snapshot()
            if usage_now is None:
                break
            month_used = int(usage_now.get("bytes_used_month") or 0)
            week_used = int(usage_now.get("bytes_used_week") or 0)
            if ((month_cap and month_cap - month_used <= month_reserve) or
                    (week_cap and week_cap - week_used <= week_reserve)):
                print("Stopping at configured byte-quota safety reserve.")
                break
        time.sleep(pause)

    remaining = db.execute("SELECT COUNT(*) FROM tasks WHERE status IN ('pending','partial')").fetchone()[0]
    blocked = db.execute("SELECT COUNT(*) FROM tasks WHERE status IN ('blocked','needs_review')").fetchone()[0]
    db.close()
    print(f"Batch complete: {request_count} data calls; pending/partial tasks={remaining:,}; blocked/review={blocked:,}.")
    print("Re-run with the same manifest to resume. Review licensing, reported account usage, and partition completeness before continuing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
