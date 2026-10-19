"""Normalize a bounded LSE sample artifact while preserving source records.

No API requests are made. Output remains local/private and is only a prototype
of a per-source canonical layer; it must not replace dataset-specific schemas.
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any


TIME_RULES = {
    "candles:": ("timestamp", "bar_start_or_provider_timestamp"),
    "series:": ("date", "reference_observation_date"),
    "options_flow:": ("ts", "option_trade_event_time"),
    "options_1m:": ("minute", "option_bar_start_time"),
    "reference:bond_yields": ("date", "reference_observation_date"),
    "reference:cot": ("date", "position_as_of_date"),
    "reference:economic_calendar": ("datetime", "scheduled_or_actual_event_time"),
    "reference:dividends": ("effective_date", "effective_date_not_release_time"),
    "reference:stock_splits": ("effective_date", "effective_date_not_release_time"),
    "reference:financial_reports": ("accepted_date", "filing_acceptance_availability_time_if_confirmed"),
    "reference:insider_trades": ("filing_date", "filing_availability_date_transaction_date_separate"),
    "reference:company_profiles": ("updated_at", "provider_snapshot_update_time"),
    "reference:stock_fundamentals": ("updated_at", "provider_snapshot_update_time"),
}


def parse_dt(value: Any) -> datetime | None:
    if value is None or value == "":
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        try:
            return datetime.combine(date.fromisoformat(str(value)[:10]), datetime.min.time())
        except (TypeError, ValueError):
            return None


def field_rule(endpoint: str) -> tuple[str | None, str]:
    for prefix, rule in TIME_RULES.items():
        if endpoint.startswith(prefix):
            return rule
    return None, "no_generic_time_rule_preserve_source_fields"


def stable_key(endpoint: str, row: dict[str, Any]) -> str:
    for key in ("id", "trade_id", "ticker"):
        if row.get(key) not in (None, ""):
            return f"{endpoint}:{key}:{row[key]}"
    encoded = json.dumps(row, sort_keys=True, separators=(",", ":"), default=str)
    return f"{endpoint}:sha256:{hashlib.sha256(encoded.encode('utf-8')).hexdigest()}"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python normalize_lse_bounded_samples.py <sample.json> [output_directory]", file=sys.stderr)
        return 2
    source = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else source.parent / "transformed_samples"
    if not source.is_file():
        print(f"Sample artifact not found: {source}", file=sys.stderr)
        return 2
    artifact = json.loads(source.read_text(encoding="utf-8"))
    rows_out: list[dict[str, Any]] = []
    family_count: Counter[str] = Counter()
    field_names: dict[str, set[str]] = defaultdict(set)
    qc = Counter()

    for result in artifact.get("results", []):
        endpoint = str(result.get("endpoint", "unknown"))
        if result.get("status") != "ok":
            qc[f"endpoint_error:{endpoint}"] += 1
            continue
        field, time_semantics = field_rule(endpoint)
        for idx, row in enumerate(result.get("sample_rows", [])):
            if not isinstance(row, dict):
                qc["non_object_sample_rows"] += 1
                continue
            family_count[endpoint] += 1
            field_names[endpoint].update(str(k) for k in row)
            ts_value = row.get(field) if field else None
            event_dt = parse_dt(ts_value)
            normalized = {
                "source_endpoint": endpoint,
                "source_retrieved_at_utc": artifact.get("retrieved_at_utc"),
                "source_row_index": idx,
                "source_record_key": stable_key(endpoint, row),
                "dataset_family": endpoint.split(":", 1)[0],
                "instrument": row.get("symbol") or row.get("underlying") or row.get("ticker"),
                "underlying": row.get("underlying"),
                "contract": row.get("ticker") if row.get("underlying") else None,
                "source_time_field": field,
                "source_time_value": ts_value,
                "source_time_semantics": time_semantics,
                "event_time_parsed_iso": event_dt.isoformat() if event_dt else None,
                "expiry": row.get("expiry"),
                "dte_reported": row.get("dte"),
                "updated_at": row.get("updated_at"),
                "last_trade_at": row.get("last_trade_at"),
                "date": row.get("date"),
                "open": row.get("open"),
                "high": row.get("high"),
                "low": row.get("low"),
                "close": row.get("close"),
                "volume": row.get("volume"),
                "value": row.get("value"),
                "currency": row.get("currency"),
                "raw_record_json": json.dumps(row, sort_keys=True, ensure_ascii=False, default=str),
            }
            if all(row.get(k) is not None for k in ("open", "high", "low", "close")):
                try:
                    op, hi, lo, cl = (float(row[k]) for k in ("open", "high", "low", "close"))
                    if lo > min(op, cl) or hi < max(op, cl) or lo > hi:
                        qc[f"ohlc_violation:{endpoint}"] += 1
                    else:
                        qc[f"ohlc_pass:{endpoint}"] += 1
                except (TypeError, ValueError):
                    qc[f"ohlc_parse_error:{endpoint}"] += 1
            if endpoint.startswith("options_chain:") and row.get("expiry"):
                try:
                    exp = date.fromisoformat(str(row["expiry"])[:10])
                    retrieved = parse_dt(artifact.get("retrieved_at_utc"))
                    asof = retrieved.date() if retrieved else None
                    last_trade = parse_dt(row.get("last_trade_at"))
                    if asof and exp < asof:
                        normalized["chain_quality_flag"] = "expired_at_sample_retrieval"
                        qc["expired_option_chain_rows"] += 1
                    elif last_trade and asof and (asof - last_trade.date()).days > 30:
                        normalized["chain_quality_flag"] = "last_trade_older_than_30d"
                        qc["stale_option_chain_rows"] += 1
                except ValueError:
                    normalized["chain_quality_flag"] = "unparseable_expiry"
                    qc["unparseable_option_expiry"] += 1
            rows_out.append(normalized)

    out.mkdir(parents=True, exist_ok=True)
    columns = sorted({key for row in rows_out for key in row})
    csv_path = out / "lse_sample_canonical_rows.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows_out)
    manifest = {
        "source_sample_artifact": source.name,
        "source_retrieved_at_utc": artifact.get("retrieved_at_utc"),
        "transformed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sdk_version": artifact.get("sdk_version"),
        "rows_transformed": len(rows_out),
        "endpoint_row_counts": dict(sorted(family_count.items())),
        "endpoint_fields_observed": {k: sorted(v) for k, v in sorted(field_names.items())},
        "quality_counts": dict(sorted(qc.items())),
        "transformations": [
            "preserve source fields as raw_record_json",
            "add family/endpoint/instrument/source-clock lineage fields",
            "no unit conversions, deduplication, backfills, or time-zone reinterpretation applied",
        ],
        "rights_note": "Private user-authorized sample processing; derived sample rows remain under source terms.",
        "output_csv": csv_path.name,
    }
    manifest_path = out / "lse_sample_transform_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Rows transformed: {len(rows_out)}")
    print(f"Canonical sample CSV: {csv_path.resolve()}")
    print(f"Transform manifest: {manifest_path.resolve()}")
    print("No API requests were made; raw source record JSON is preserved in each output row.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
