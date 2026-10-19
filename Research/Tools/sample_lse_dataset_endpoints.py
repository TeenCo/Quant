"""Sample LSE endpoint schemas with strict per-request row limits.

This is a diagnostic sample, not a bulk exporter. It reads local catalog and
preflight JSON, prompts for the API key invisibly, and caps each query to 3 rows
(option chain/flow also capped). It never calls history(), dataset(), or stream().

Usage:
    python sample_lse_dataset_endpoints.py <catalog.json> <preflight.json> [output_dir]
"""

from __future__ import annotations

import getpass
import json
import sys
import time
from datetime import date, datetime, timedelta, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any, Callable


def safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {str(k): safe(v) for k, v in value.items()
                if str(k).lower() not in {"api_key", "authorization", "token", "secret", "password"}}
    if isinstance(value, (list, tuple)):
        return [safe(v) for v in value]
    return str(value)


def describe(rows: Any) -> dict[str, Any]:
    if not isinstance(rows, list):
        rows = [rows]
    rows = rows[:3]
    field_types: dict[str, set[str]] = {}
    for row in rows:
        if isinstance(row, dict):
            for key, value in row.items():
                field_types.setdefault(str(key), set()).add(type(value).__name__)
    return {
        "sample_row_count": len(rows),
        "fields": {key: sorted(types) for key, types in sorted(field_types.items())},
        "sample_rows": safe(rows),
    }


def bounded_call(results: list[dict[str, Any]], label: str, fn: Callable[[], Any]) -> Any:
    try:
        rows = fn()
        results.append({"endpoint": label, "status": "ok", **describe(rows)})
        return rows
    except Exception as exc:
        entry = {"endpoint": label, "status": "error", "error_type": type(exc).__name__}
        status = getattr(exc, "status", None)
        if isinstance(status, (int, str)):
            entry["http_status"] = status
        results.append(entry)
        return None


def representative(catalog: list[dict[str, Any]], dataset: str) -> dict[str, Any] | None:
    candidates = [r for r in catalog if r.get("dataset") == dataset and r.get("symbol")]
    if not candidates:
        return None
    return max(candidates, key=lambda r: int(r.get("ticks") or 0))


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python sample_lse_dataset_endpoints.py <catalog.json> <preflight.json> [output_dir]", file=sys.stderr)
        return 2
    catalog_path, preflight_path = Path(sys.argv[1]), Path(sys.argv[2])
    out = Path(sys.argv[3]) if len(sys.argv) > 3 else catalog_path.parent / "bounded_samples"
    if not catalog_path.is_file() or not preflight_path.is_file():
        print("Catalog or preflight JSON was not found; no API request was made.", file=sys.stderr)
        return 2
    catalog_payload = json.loads(catalog_path.read_text(encoding="utf-8"))
    preflight = json.loads(preflight_path.read_text(encoding="utf-8"))
    catalog = catalog_payload.get("catalog", [])
    meta = preflight.get("metadata", {}).get("vault_meta", {})
    usage = preflight.get("metadata", {}).get("usage", {})
    print("Account preflight usage:", json.dumps(usage, sort_keys=True))
    print("This run will make bounded sample queries (maximum 3 rows per call), not exports.")
    confirm = input("Type SAMPLE to continue: ").strip()
    if confirm != "SAMPLE":
        print("Cancelled; no API key was requested and no sample calls were made.")
        return 0

    try:
        from lse import LSE
    except ImportError:
        print("Missing SDK. Install with: python -m pip install lse-data", file=sys.stderr)
        return 2
    key = getpass.getpass("LSE API key (input hidden): ").strip()
    if not key:
        print("No key entered; no API request was made.", file=sys.stderr)
        return 2
    try:
        client = LSE(api_key=key)
    except Exception as exc:
        key = ""
        print(f"Client initialization failed ({type(exc).__name__}); details suppressed.", file=sys.stderr)
        return 1
    key = ""

    results: list[dict[str, Any]] = []
    # One bounded daily-candle sample for each candle/synthetic-candle class.
    candle_classes = list(dict.fromkeys(meta.get("candle_classes", []) + meta.get("synth_candle_classes", [])))
    for dataset in candle_classes:
        row = representative(catalog, dataset)
        if not row:
            results.append({"endpoint": f"candles:{dataset}", "status": "no_catalog_symbol"})
            continue
        bounded_call(results, f"candles:{dataset}:{row['symbol']}",
                     lambda row=row, dataset=dataset: client.candles(
                         row["symbol"], timeframe="1d", limit=3, order="desc", dataset=dataset))
        time.sleep(0.7)

    # One short recent series sample for each series class.
    for dataset in meta.get("series_classes", []):
        row = representative(catalog, dataset)
        if not row:
            results.append({"endpoint": f"series:{dataset}", "status": "no_catalog_symbol"})
            continue
        bounded_call(results, f"series:{dataset}:{row['symbol']}",
                     lambda row=row, dataset=dataset: client.series(
                         row["symbol"], dataset=dataset, order="desc", limit=3))
        time.sleep(0.7)

    # Bounded current chain and recent prints for one cataloged option underlying.
    option_row = representative(catalog, "options")
    underlying = option_row.get("symbol") if option_row else None
    chain = None
    if underlying and meta.get("options", {}).get("chain"):
        chain = bounded_call(results, f"options_chain:{underlying}",
                             lambda: client.options(underlying, max_dte=30, limit=3))
        time.sleep(0.7)
    if underlying and meta.get("options", {}).get("flow"):
        bounded_call(results, f"options_flow:{underlying}",
                     lambda: client.options_flow(underlying=underlying, limit=3))
        time.sleep(0.7)
    if chain and meta.get("options", {}).get("flow_1m"):
        contract = None
        if isinstance(chain, list) and chain and isinstance(chain[0], dict):
            for key_name in ("ticker", "symbol", "option_symbol", "osi"):
                if chain[0].get(key_name):
                    contract = chain[0][key_name]
                    break
        if contract:
            bounded_call(results, f"options_1m:{contract}",
                         lambda: client.option_candles(contract, limit=3, order="desc"))
        else:
            results.append({"endpoint": "options_1m", "status": "skipped_no_contract_identifier_in_chain_sample"})

    # Bounded rows from reference-data methods. Reference inventory count/span
    # comes from preflight; these examples test schema, not coverage completeness.
    today = date.today()
    month_ago = (today - timedelta(days=30)).isoformat()
    year_ago = (today - timedelta(days=365)).isoformat()
    refs = preflight.get("metadata", {}).get("reference_inventory", [])
    ref_names = {r.get("dataset") for r in refs if isinstance(r, dict)}
    calls: list[tuple[str, Callable[[], Any]]] = []
    if "bond_yields" in ref_names:
        calls.append(("reference:bond_yields", lambda: client.bond_yields(symbol="US10Y", order="desc", limit=3)))
    if "company_profiles" in ref_names:
        calls.append(("reference:company_profiles", lambda: client.company_profiles(symbol="AAPL", limit=3)))
    if "cot" in ref_names:
        calls.append(("reference:cot", lambda: client.cot(symbol="GC", start=year_ago, end=today.isoformat(), order="desc", limit=3)))
    if "dividends" in ref_names:
        calls.append(("reference:dividends", lambda: client.dividends(symbol="AAPL", start=year_ago, end=today.isoformat(), order="desc", limit=3)))
    if "economic_calendar" in ref_names:
        calls.append(("reference:economic_calendar", lambda: client.economic_calendar(region="US", start=month_ago, end=today.isoformat(), order="desc", limit=3)))
    if "financial_reports" in ref_names:
        calls.append(("reference:financial_reports", lambda: client.financial_reports(symbol="AAPL", report_type="income", period="FY", order="desc", limit=3)))
    if "insider_trades" in ref_names:
        calls.append(("reference:insider_trades", lambda: client.insider_trades(symbol="AAPL", start=year_ago, end=today.isoformat(), order="desc", limit=3)))
    if "stock_fundamentals" in ref_names:
        calls.append(("reference:stock_fundamentals", lambda: client.fundamentals(symbol="AAPL", limit=3)))
    if "stock_splits" in ref_names:
        calls.append(("reference:stock_splits", lambda: client.splits(symbol="AAPL", start=year_ago, end=today.isoformat(), order="desc", limit=3)))
    for label, call in calls:
        bounded_call(results, label, call)
        time.sleep(0.7)

    out.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    artifact = {
        "source_catalog": catalog_path.name,
        "source_preflight": preflight_path.name,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sdk_version": _sdk_version(),
        "history_or_bulk_export_called": False,
        "maximum_sample_rows_per_call": 3,
        "sample_call_count": len(results),
        "results": results,
        "terms": "Private research artifact; do not redistribute LSE-derived records outside current provider permissions.",
    }
    path = out / f"lse_bounded_endpoint_samples_{stamp}.json"
    path.write_text(json.dumps(artifact, indent=2, ensure_ascii=False), encoding="utf-8")
    ok = sum(r.get("status") == "ok" for r in results)
    errs = sum(r.get("status") == "error" for r in results)
    print(f"Sample calls recorded: {len(results)}; successful: {ok}; errors: {errs}")
    print(f"Local private sample artifact: {path.resolve()}")
    print("No history(), dataset(), or stream() call was made.")
    return 0 if errs == 0 else 1


def _sdk_version() -> str:
    try:
        return version("lse-data")
    except PackageNotFoundError:
        return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
