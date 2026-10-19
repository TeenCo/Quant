# Run the LSE Daily-Candle and Series Sync

This guide covers [[sync_lse_daily_and_series.py]], a resumable local downloader for the user's selected **1d candle history plus full series observations**. It does not download raw tick history, options flow, reference tables, or live streams. Data files remain outside the Obsidian vault.

## Preview first

Using the installed `.venv` SDK and local catalog/preflight snapshots:

```powershell
python "Research\Tools\sync_lse_daily_and_series.py" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\lse_catalog_20261018T135141Z.json" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\preflight\lse_metadata_preflight_20261018T135558Z.json" `
  --out "C:\Users\Dell\Desktop\Quant\lse_daily_series"
```

Default mode creates a SQLite task manifest only. The current manifest contains 4,243 1d candle symbols plus 15,537 series symbols (19,780 tasks). Date bounds come from catalog metadata and are capped at snapshot date; they are provisional until sample semantics are confirmed. One request per task is a rough lower bound; results capped at 5,000 rows are paginated and checkpointed.

## Execute one bounded batch

Only after terms, desired coverage, disk space, and current account usage are reviewed, start with `--execute --max-calls 10` to measure actual response sizes and inspect partitions. The script requests a second phrase (`FETCH DAILY/SERIES`), then prompts for the API key invisibly. It checks the current usage endpoint before calls, preserves byte safety reserves, paces requests, and stops after the chosen call cap or quota reserve. It writes JSONL partitions and SQLite progress, not Parquet, and resumes on rerun. After reviewing the first batch's sizes/QC, a larger user-selected call cap can reduce repeated manual restarts.

```powershell
python "Research\Tools\sync_lse_daily_and_series.py" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\lse_catalog_20261018T135141Z.json" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\preflight\lse_metadata_preflight_20261018T135558Z.json" `
  --out "C:\Users\Dell\Desktop\Quant\lse_daily_series" `
  --execute --max-calls 40
```

Never put the key in command-line arguments or share the data directory. Inspect the manifest and compare quotas after each batch. The first pass is a large local-data operation; begin with a modest call cap and representative family outputs.

The first 10-call user pilot completed six symbol tasks and 28,475 rows with no duplicate keys or basic OHLC bounds errors. After reviewing that pilot, a larger batch may be run with `--max-calls 1000` (roughly 7 minutes at the configured pacing, plus endpoint latency), subject to current quota/disk checks. Repeat against the same manifest/output path until every task is complete, empty, blocked, or deliberately excluded; then reconcile against the catalog and record the unresolved statuses.

Transient transport/server statuses (0, 408, 429, 500, 502, 503, 504) now receive up to two exponential-backoff retries. A persistent failure is marked `blocked` and the batch stops. Normal reruns skip blocked tasks and continue with pending work; add `--retry-blocked` only when deliberately retrying blocked tasks with one of these transient status codes.

The `/usage` endpoint is polled at startup and every 500 completed calls by default (`--usage-check-every 0` disables periodic checks). A 429 from `/usage` now gets short backoff retries instead of stopping the batch; if usage still cannot be read, the run stops safely before the next data batch.

## Reference tables are a separate export queue

The SDK's `dataset()` path launches Parquet export jobs. The account snapshot allows five jobs/hour and has weekly/monthly byte caps. Use [[Tools/Plan and run LSE reference exports]] to create a partitioned queue and execute at most one or a few explicitly confirmed jobs per invocation. Large options-flow tables are daily-partitioned in the plan because provider inventory lists hundreds of millions of rows; estimated sizes are unknown, so monitor file sizes/usage and stop if safety reserves are approached.

## Interpretation limits

The sync output preserves returned fields and lineage but does not establish source correctness, full universe/contract completeness, point-in-time revisions, or executable fills. Do not generate research features until schema, timestamp semantics, independent spot checks, and data rights are documented for each family. See [[Exhaustive dataset inventory and transformation protocol]].
