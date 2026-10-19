"""Analyze an LSE catalog snapshot; does not make provider requests.

Usage:
    python analyze_lse_catalog.py <catalog.json> [output_directory]

Outputs a locally generated Markdown coverage report and a row-level CSV with
catalog-derived flags. These outputs remain subject to LSE data terms.
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_date(value: Any) -> datetime | None:
    if not value:
        return None
    text = str(value).strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is not None:
        return dt.astimezone(timezone.utc).replace(tzinfo=None)
    # Catalog timestamps have no declared zone in the response; do not imply UTC.
    return dt


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python analyze_lse_catalog.py <catalog.json> [output_directory]", file=sys.stderr)
        return 2
    source = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else source.parent / "analysis"
    if not source.is_file():
        print(f"Catalog file not found: {source}", file=sys.stderr)
        return 2
    payload = json.loads(source.read_text(encoding="utf-8"))
    rows = payload.get("catalog")
    if not isinstance(rows, list):
        print("Expected catalog JSON object containing a 'catalog' list.", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    retrieved = payload.get("retrieved_at_utc")
    snapshot_dt = parse_date(retrieved)
    snapshot_day = snapshot_dt.date() if snapshot_dt else None

    enriched: list[dict[str, Any]] = []
    category_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    dataset_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    country_counts: Counter[str] = Counter()
    seen_keys: Counter[tuple[str, str]] = Counter()
    missing = Counter()
    future_last: list[dict[str, Any]] = []
    future_first: list[dict[str, Any]] = []
    reversed_ranges: list[dict[str, Any]] = []
    negative_ticks: list[dict[str, Any]] = []

    for original in rows:
        if not isinstance(original, dict):
            continue
        r = dict(original)
        category = str(r.get("category") or "UNKNOWN")
        dataset = str(r.get("dataset") or "UNKNOWN")
        symbol = str(r.get("symbol") or "")
        first_dt = parse_date(r.get("first"))
        last_dt = parse_date(r.get("last"))
        ticks = r.get("ticks")
        try:
            tick_count = int(ticks) if ticks is not None else None
        except (TypeError, ValueError):
            tick_count = None
        key = (dataset, symbol)
        seen_keys[key] += 1
        for field in ("symbol", "name", "category", "dataset", "ticks", "first", "last"):
            if r.get(field) in (None, ""):
                missing[field] += 1
        if r.get("country") in (None, ""):
            missing["country"] += 1
        else:
            country_counts[str(r["country"])] += 1
        if snapshot_day and last_dt and last_dt.date() > snapshot_day:
            future_last.append(r)
        if snapshot_day and first_dt and first_dt.date() > snapshot_day:
            future_first.append(r)
        if first_dt and last_dt and first_dt > last_dt:
            reversed_ranges.append(r)
        if tick_count is not None and tick_count < 0:
            negative_ticks.append(r)

        r["catalog_retrieved_at_utc"] = retrieved
        r["catalog_last_after_snapshot_date"] = bool(snapshot_day and last_dt and last_dt.date() > snapshot_day)
        r["catalog_first_after_snapshot_date"] = bool(snapshot_day and first_dt and first_dt.date() > snapshot_day)
        r["catalog_range_parse_status"] = "parsed" if first_dt and last_dt else "missing_or_unparseable"
        r["catalog_availability_class"] = "unknown_from_catalog_alone"
        r["rights_status"] = "not_verified_for_dataset"
        r["schema_status"] = "catalog_fields_only"
        r["acquisition_status"] = "not_requested"
        r["next_action"] = "review_terms_schema_clock_then_sample"
        enriched.append(r)
        category_groups[category].append(r)
        dataset_groups[dataset].append(r)

    duplicate_groups = {k: c for k, c in seen_keys.items() if c > 1}
    total_ticks = sum(int(r.get("ticks") or 0) for r in rows if str(r.get("ticks") or "").isdigit())

    csv_path = out / "lse_catalog_enriched.csv"
    columns = sorted({str(k) for r in enriched for k in r})
    with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(enriched)

    report: list[str] = [
        "# LSE Catalog Coverage Report",
        "",
        f"- **Source snapshot:** `{source.name}`",
        f"- **Retrieved at UTC (per helper):** `{retrieved or 'not recorded'}`",
        f"- **SDK version:** `{payload.get('sdk_version', 'unknown')}`",
        f"- **Rows returned:** {len(rows):,}",
        f"- **Unique (dataset, symbol) keys:** {len(seen_keys):,}",
        f"- **Duplicate key groups:** {len(duplicate_groups):,}",
        f"- **Catalog tick-count sum:** {total_ticks:,} (provider metadata only; not a downloaded-row count or completeness proof)",
        f"- **Rows with last date after snapshot date:** {len(future_last):,}",
        f"- **Rows with first date after snapshot date:** {len(future_first):,}",
        f"- **Reversed first/last ranges:** {len(reversed_ranges):,}",
        f"- **Negative tick counts:** {len(negative_ticks):,}",
        "",
        "> Catalog `first`, `last`, and `ticks` are provider metadata. Their semantics, timezone, truncation, revision behavior, and completeness require SDK/provider confirmation and sampled endpoint validation. A catalog does not establish that all history can be exported or legally retained.",
        "",
        "## By category",
        "",
        "| Category | Catalog rows | Distinct datasets | Distinct countries | Tick metadata sum | Earliest `first` | Latest `last` | Future-last rows |",
        "|---|---:|---:|---:|---:|---|---|---:|",
    ]
    for category, group in sorted(category_groups.items(), key=lambda x: x[0].lower()):
        firsts = [str(r["first"]) for r in group if r.get("first")]
        lasts = [str(r["last"]) for r in group if r.get("last")]
        report.append(
            f"| {category} | {len(group):,} | {len({r.get('dataset') for r in group}):,} | "
            f"{len({r.get('country') for r in group if r.get('country')}):,} | "
            f"{sum(int(r.get('ticks') or 0) for r in group if str(r.get('ticks') or '').isdigit()):,} | "
            f"{min(firsts) if firsts else '—'} | {max(lasts) if lasts else '—'} | "
            f"{sum(bool(r.get('catalog_last_after_snapshot_date')) for r in group):,} |"
        )
    report += ["", "## By dataset", "", "| Dataset | Catalog rows | Earliest `first` | Latest `last` | Tick metadata sum | Countries | Future-last rows |", "|---|---:|---|---|---:|---:|---:|"]
    for dataset, group in sorted(dataset_groups.items(), key=lambda x: x[0].lower()):
        firsts = [str(r["first"]) for r in group if r.get("first")]
        lasts = [str(r["last"]) for r in group if r.get("last")]
        report.append(
            f"| {dataset} | {len(group):,} | {min(firsts) if firsts else '—'} | {max(lasts) if lasts else '—'} | "
            f"{sum(int(r.get('ticks') or 0) for r in group if str(r.get('ticks') or '').isdigit()):,} | "
            f"{len({r.get('country') for r in group if r.get('country')}):,} | "
            f"{sum(bool(r.get('catalog_last_after_snapshot_date')) for r in group):,} |"
        )
    report += ["", "## Field completeness", "", "| Field | Missing/blank rows |", "|---|---:|"]
    for field in ("symbol", "name", "category", "dataset", "ticks", "first", "last", "country"):
        report.append(f"| {field} | {missing[field]:,} |")
    report += ["", "## Review flags", ""]
    if duplicate_groups:
        report.append(f"- Investigate {len(duplicate_groups):,} duplicate `(dataset, symbol)` key groups; see the enriched CSV.")
    else:
        report.append("- No duplicate `(dataset, symbol)` keys detected in this snapshot.")
    if future_last:
        report.append(f"- {len(future_last):,} rows have `last` later than the catalog snapshot date. Some may be forecast/calendar series; audit these before treating `last` as an observed-data boundary.")
    if future_first:
        report.append(f"- {len(future_first):,} rows have `first` later than the snapshot date; investigate whether these are scheduled/forecast series or catalog errors.")
    if reversed_ranges:
        report.append(f"- {len(reversed_ranges):,} rows have a first date later than last date; investigate provider semantics or malformed metadata.")
    if negative_ticks:
        report.append(f"- {len(negative_ticks):,} rows have negative tick counts; investigate before interpreting count fields.")
    report += [
        "- Catalog metadata does not show native resolution, timestamp timezone, quote/trade definition, exportability, license per dataset, or point-in-time/revision status; obtain these from product documentation/small authorized sample before ranking acquisition priority.",
        "- `ticks` values may measure provider-side records in a way that differs by dataset; do not sum them as observations acquired or use them as a data-completeness metric.",
        "",
        "## Acquisition decision",
        "",
        "Do not export all rows at once. First classify datasets by rights, research relevance, schema, point-in-time availability, and estimated export cost. Then sample one dataset per type, verify schema and terms, estimate total jobs/storage, and build a partition reconciliation ledger. Use [[Exhaustive dataset inventory and transformation protocol]].",
        "",
        f"Row-level enriched catalog: `{csv_path.name}`",
    ]
    report_path = out / "lse_catalog_coverage_report.md"
    report_path.write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"Rows: {len(rows):,}; categories: {len(category_groups)}; datasets: {len(dataset_groups)}")
    print(f"Coverage report: {report_path.resolve()}")
    print(f"Enriched catalog: {csv_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
