"""Collect LSE metadata and account usage without exporting market history.

Usage:
    python -m pip install lse-data
    python lse_metadata_preflight.py [output_directory]

Prompts for the API key without echoing it. Calls only metadata endpoints:
catalog, vault metadata, reference-dataset inventory, and usage. Does not call
history(), dataset(), candles(), series(), options(), or any stream.
"""

from __future__ import annotations

import getpass
import json
import sys
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Any


def safe(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {
            str(k): safe(v) for k, v in value.items()
            if str(k).lower() not in {"api_key", "authorization", "token", "secret", "password"}
        }
    if isinstance(value, (list, tuple)):
        return [safe(v) for v in value]
    return str(value)


def main() -> int:
    try:
        from lse import LSE
    except ImportError:
        print("Missing SDK. Install with: python -m pip install lse-data", file=sys.stderr)
        return 2

    key = getpass.getpass("LSE API key (input hidden): ").strip()
    if not key:
        print("No API key entered; no request was made.", file=sys.stderr)
        return 2

    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("lse_catalog_snapshot") / "preflight"
    out.mkdir(parents=True, exist_ok=True)
    result: dict[str, Any] = {
        "source": "LSE metadata preflight",
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sdk_version": _sdk_version(),
        "history_downloaded": False,
        "metadata": {},
        "errors": [],
    }
    try:
        client = LSE(api_key=key)
        for label, call in (
            ("vault_meta", client.vault_meta),
            ("catalog", client.catalog),
            ("reference_inventory", client.reference),
            ("usage", lambda: client._vault_call("/usage")),
        ):
            try:
                value = safe(call())
                result["metadata"][label] = value
                if label == "catalog" and isinstance(value, list):
                    result["catalog_row_count"] = len(value)
            except Exception as exc:
                # Suppress exception text because SDK errors may include request details.
                item = {"endpoint": label, "error_type": type(exc).__name__}
                status = getattr(exc, "status", None)
                if isinstance(status, (int, str)):
                    item["http_status"] = status
                result["errors"].append(item)
    finally:
        key = ""

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = out / f"lse_metadata_preflight_{stamp}.json"
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Metadata snapshot: {path.resolve()}")
    print(f"Catalog rows: {result.get('catalog_row_count', 'not retrieved')}")
    print(f"Metadata endpoint errors: {len(result['errors'])}")
    print("No historical data or live ticks were requested.")
    return 0 if not result["errors"] else 1


def _sdk_version() -> str:
    try:
        return version("lse-data")
    except PackageNotFoundError:
        return "unknown"


if __name__ == "__main__":
    raise SystemExit(main())
