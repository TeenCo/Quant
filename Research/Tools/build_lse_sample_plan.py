"""Build a local bounded sample plan from an LSE catalog snapshot; no requests."""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


def dt(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python build_lse_sample_plan.py <catalog.json> [output_directory]", file=sys.stderr)
        return 2
    source = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else source.parent / "sample_plan"
    if not source.is_file():
        print(f"Catalog file not found: {source}", file=sys.stderr)
        return 2
    payload = json.loads(source.read_text(encoding="utf-8"))
    rows = payload.get("catalog", [])
    snapshot_dt = dt(payload.get("retrieved_at_utc"))
    snapshot_date = snapshot_dt.date() if snapshot_dt else None
    groups: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        groups.setdefault(str(row.get("dataset") or "UNKNOWN"), []).append(row)

    plan: list[dict[str, Any]] = []
    for dataset, group in sorted(groups.items()):
        valid = [r for r in group if r.get("symbol")]
        # Cover scale, typical history, and oldest available start without pulling all symbols.
        by_ticks = sorted(valid, key=lambda r: int(r.get("ticks") or 0))
        earliest = sorted(valid, key=lambda r: dt(r.get("first")) or datetime.max)
        picks: list[tuple[str, dict[str, Any]]] = []
        if by_ticks:
            picks.append(("largest_catalog_tick_count", by_ticks[-1]))
            picks.append(("median_catalog_tick_count", by_ticks[len(by_ticks) // 2]))
        if earliest:
            picks.append(("earliest_catalog_history", earliest[0]))
        unique: set[str] = set()
        for reason, row in picks:
            symbol = str(row["symbol"])
            if symbol in unique:
                continue
            unique.add(symbol)
            last_dt = dt(row.get("last"))
            if last_dt and last_dt.tzinfo is not None:
                last_dt = last_dt.replace(tzinfo=None)
            if last_dt and snapshot_date and last_dt.date() > snapshot_date:
                # Do not propose a window ending in a catalog future date.
                last_dt = datetime.combine(snapshot_date, datetime.min.time())
            if last_dt:
                start_dt = last_dt - timedelta(days=7)
                start = start_dt.date().isoformat()
                end = last_dt.date().isoformat()
            else:
                start = end = ""
            if dataset == "options":
                method = "chain_discovery_only; options(underlying, max_dte=30, limit<=20); then select one OSI contract"
                timeframe = "not applicable"
            elif dataset in {"economics", "bonds", "sovereign_yields", "interest_rates"}:
                method = "series(symbol, dataset=dataset, start, end, limit<=100)"
                timeframe = "native series frequency; inspect result"
            else:
                method = "candles(symbol, timeframe=1d, start, end, limit<=20, dataset=dataset)"
                timeframe = "1d"
            plan.append({
                "dataset": dataset,
                "symbol": symbol,
                "name": row.get("name"),
                "category": row.get("category"),
                "selection_reason": reason,
                "catalog_ticks_metadata": row.get("ticks"),
                "catalog_first": row.get("first"),
                "catalog_last": row.get("last"),
                "sample_start_date_candidate": start,
                "sample_end_date_candidate": end,
                "timeframe_candidate": timeframe,
                "method_candidate": method,
                "execution_status": "planned_only_not_requested",
                "preconditions": "Confirm terms, usage quota, endpoint/schema, timestamp semantics, and that catalog dates are not projections before running.",
            })

    out.mkdir(parents=True, exist_ok=True)
    json_path = out / "lse_representative_sample_plan.json"
    csv_path = out / "lse_representative_sample_plan.csv"
    json_path.write_text(json.dumps({
        "source_snapshot": source.name,
        "source_retrieved_at_utc": payload.get("retrieved_at_utc"),
        "planned_rows": len(plan),
        "requests_made": 0,
        "plan": plan,
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    columns = list(plan[0]) if plan else []
    if columns:
        with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns)
            writer.writeheader()
            writer.writerows(plan)
    print(f"Sample candidates: {len(plan)} across {len(groups)} datasets")
    print(f"JSON plan: {json_path.resolve()}")
    print(f"CSV plan: {csv_path.resolve()}")
    print("No API requests or data exports were made.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
