"""Create a local snapshot of the LSE catalog (metadata only; no market history).

Usage:
    python -m pip install lse-data
    python inventory_lse_catalog.py [output_directory]

The API key is requested with getpass and is never written to output. Store the
result locally and do not redistribute it unless current provider terms allow.
This script deliberately does not call history(), dataset(), candles(), or stream().
"""

from __future__ import annotations

import csv
import getpass
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def json_safe(value: Any) -> Any:
    """Convert nested SDK values to JSON-safe structures without secret fields."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {
            str(key): json_safe(item)
            for key, item in value.items()
            if str(key).lower() not in {"api_key", "authorization", "token", "secret"}
        }
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if hasattr(value, "__dict__"):
        return json_safe(vars(value))
    return str(value)


def main() -> int:
    try:
        from lse import LSE, LSEError
    except ImportError:
        print("Missing dependency. Install with: python -m pip install lse-data", file=sys.stderr)
        return 2

    key = getpass.getpass("LSE API key (input hidden): ").strip()
    if not key:
        print("No API key entered; no request was made.", file=sys.stderr)
        return 2

    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("lse_catalog_snapshot")
    output_dir.mkdir(parents=True, exist_ok=True)
    retrieved_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    try:
        client = LSE(api_key=key)
        rows = client.catalog()
    except LSEError as exc:
        # Do not print exception text: SDK/network errors can contain request details.
        print(f"LSE catalog request failed (status={getattr(exc, 'status', 'unknown')}).", file=sys.stderr)
        return 1
    except Exception as exc:  # SDK/network exceptions vary by version.
        print(f"Catalog request failed ({type(exc).__name__}); details suppressed.", file=sys.stderr)
        return 1
    finally:
        key = ""  # Drop the local reference as soon as the request completes.

    safe_rows = json_safe(rows)
    if not isinstance(safe_rows, list):
        print(f"Unexpected catalog response type: {type(safe_rows).__name__}", file=sys.stderr)
        return 1

    snapshot = {
        "source": "London Strategic Edge SDK catalog",
        "retrieved_at_utc": retrieved_at,
        "sdk_version": _sdk_version(),
        "row_count": len(safe_rows),
        "data_history_downloaded": False,
        "catalog": safe_rows,
    }
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    json_path = output_dir / f"lse_catalog_{stamp}.json"
    json_path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")

    dict_rows = [row for row in safe_rows if isinstance(row, dict)]
    if dict_rows:
        columns = sorted({str(key) for row in dict_rows for key in row})
        csv_path = output_dir / f"lse_catalog_{stamp}.csv"
        with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(dict_rows)
        print(f"Catalog rows: {len(safe_rows)}")
        print(f"JSON snapshot: {json_path.resolve()}")
        print(f"CSV inventory: {csv_path.resolve()}")
    else:
        print(f"Catalog rows: {len(safe_rows)}")
        print(f"JSON snapshot: {json_path.resolve()}")

    print("No historical prices, option records, reference datasets, or live ticks were requested.")
    print("Review current LSE terms and account quota before any later export or redistribution.")
    return 0


def _sdk_version() -> str:
    try:
        from importlib.metadata import PackageNotFoundError, version

        try:
            return version("lse-data")
        except PackageNotFoundError:
            return "unknown"
    except ImportError:
        return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
