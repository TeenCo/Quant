# London Strategic Edge `lse-data` SDK

## Source record

- **Author / organization:** London Strategic Edge
- **Type:** Provider-published software documentation and package metadata.
- **Links:** [GitHub repository](https://github.com/londonstrategicedge/lse-data) · [README](https://raw.githubusercontent.com/londonstrategicedge/lse-data/main/README.md) · [pyproject.toml](https://raw.githubusercontent.com/londonstrategicedge/lse-data/main/pyproject.toml)
- **Checked:** 2026-10-18
- **Evidence grade:** 5 for product feature/access and SDK usage claims; code/package metadata is direct evidence of package dependencies but does not independently validate data quality or historical completeness.
- **Recency:** Repository documentation checked 2026-10-18; package/server limits can change.
- **Novelty:** Low; a provider-specific access/workflow reference.
- **Source type:** Vendor software documentation and source repository metadata.
- **License note:** README states MIT license applies to the SDK only. Retrieved data is subject to LSE terms; README says data may not be redistributed/resold or made available to third parties.

## What the README documents

- Install via `pip install lse-data`.
- Python package requires Python `>=3.8`; core dependency metadata lists `websockets>=11.0`.
- Optional `frames` extra adds `pyarrow>=14` and `pandas>=1.5` for DataFrame-friendly Parquet pulls.
- One API key is used for REST history/data calls and WebSocket streaming.
- Key can be passed as `api_key=...` or loaded from `LSE_API_KEY`.
- README describes catalog, candles, economic series, reference datasets, options methods, bulk Parquet `history()`/`dataset()` exports, usage endpoint, and live streaming.
- README states streaming and downloads share allowances and that bulk export calls count as export jobs; confirm current live limits.

## Review notes

These are vendor-maintained claims and may change between package versions. The README page is authoritative for the examples it currently publishes, while independent coverage/accuracy tests are still required. Check the installed package version and current API schema before reproducing examples. See [[Data/London Strategic Edge]] for a complete walk-through and sample quality checklist.
