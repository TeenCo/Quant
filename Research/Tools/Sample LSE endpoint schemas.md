# Sample LSE Endpoint Schemas

This is the next operational phase after catalog and account preflight. It makes a small set of **bounded row queries** (up to three rows per call) to characterize schemas, not to download historical datasets.

## Preflight from the authorized account

The 2026-10-18 local preflight reports:

- **18 catalog dataset classes**.
- **7 candle classes** and **3 synthetic candle classes**, with 14 documented general resolutions.
- **7 series classes**; the metadata specifically lists bonds at 1d/1h resolution.
- Options chain/flow/1m-flow capabilities and 10 option-candle timeframes.
- Reference inventory metadata for 12 named tables, including counts/spans.
- Usage fields returned by the account: 0 bytes used at that snapshot, 50 GiB monthly cap, 15 GiB weekly cap, 0 of 5 export jobs used that hour, 200 calls/minute, 5,000 maximum rows/request, concurrency 2, and `historical_data_months=-1` as the raw server value. The meaning of -1 is not inferred here; confirm it in the provider account/docs.

These numbers describe the account **at the preflight timestamp** and may change. Reference-row totals (for example options flow) are provider-side inventory metadata, not what has been downloaded. Exports have separate hourly and byte budgets; do not infer the size of a full pull from catalog tick counts.

## Run bounded schema probes

Use the local `lse-data` virtual environment, current catalog and preflight snapshot:

```powershell
python "Research\Tools\sample_lse_dataset_endpoints.py" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\lse_catalog_YYYYMMDDTHHMMSSZ.json" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\preflight\lse_metadata_preflight_YYYYMMDDTHHMMSSZ.json" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\bounded_samples"
```

Review the plan: type `SAMPLE` only if you approve the bounded requests. It then prompts for the key without echoing it. The helper samples at most 3 rows per query for candle classes, series classes, one option underlying/chain/flow, and selected reference methods reported by preflight. It never calls `history()`, `dataset()`, or `stream()`; no bulk export job is started.

The output is a local private JSON file with field names/types, up to 3 sample rows, error status (message text suppressed), SDK version, and timestamp. Treat rows as LSE data and do not move them to a shared repository/vault unless current terms permit.

To demonstrate a lineage-preserving canonical sample shape without API requests, run [[Tools/normalize_lse_bounded_samples.py]] on the resulting JSON. It preserves each original response row in `raw_record_json`, adds source/clock fields, and flags basic OHLC/expired-chain issues. Its output is only a sample prototype, not a production transformer.

## Interpretation and follow-up

- A successful 3-row query validates only that one method/symbol/time slice was returned, not the full history, every catalog symbol, revision behavior, completeness, or point-in-time status.
- A method may not support a category despite `vault_meta` declaring a class; errors should be recorded, not silently treated as empty data.
- Reference sample method hints and symbol conventions can fail; verify them against current SDK methods and account docs.
- Review every successful sample's field names, timestamps, units, nulls, sorting, duplicates, first/last observed dates, and meaning against independent/official sources where available.
- Only after the schema/terms review should the sample plan be revised into bounded acquisition partitions with a complete status ledger.

Related: [[LSE catalog coverage review 2026-10-18]] · [[Exhaustive dataset inventory and transformation protocol]] · [[London Strategic Edge]] · [[Data provenance and point-in-time]] · [[Data validation patterns]] · [[Research pipeline architecture]]
