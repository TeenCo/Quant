# LSE Daily/Series Acquisition Pilot — 2026-10-18

This pilot records the first user-run batch from the resumable 1d candle/series downloader. It is **not** the full dataset extraction.

## Scope and provenance

- **Source:** user's authorized LSE SDK/account, version 0.14.0.
- **Catalog:** `lse_catalog_20261018T135141Z.json`; preflight snapshot `lse_metadata_preflight_20261018T135558Z.json`.
- **Run:** user executed `sync_lse_daily_and_series.py --execute --max-calls 10` and confirmed with `FETCH DAILY/SERIES`.
- **API activity:** ten bounded synchronous 1d-candle calls; no history(), dataset(), or stream() operation. Per-request cap: 5,000 rows.
- **Output:** private local JSONL partitions and SQLite manifest under `C:\Users\Dell\Desktop\Quant\lse_daily_series`; not copied to this vault.

## Result

The first ten calls covered BTC/USD, ETH/USD, four FX pairs, and returned **28,475 rows** across six completed instrument tasks and ten partitions. Four 5,000-row FX responses reached the endpoint limit and were continued from the next observed date; the resulting tasks completed without overlap. The other samples returned 3,194 daily rows each for the two crypto instruments. Local output was approximately 10.6 MB.

Local validation across this pilot found:

- 0 duplicate `(dataset, symbol, timestamp)` keys.
- 0 basic OHLC range violations (`low <= open/close <= high`).
- No backwards timestamp sequences within each checked partition.
- 6 complete candle tasks; 19,774 daily/series tasks remain in the SQLite manifest.

These checks validate file structure and simple invariants only. They do not establish correct prices, completeness, point-in-time availability, volume meaning, or independent accuracy. The catalog dates and SDK UTC timestamp behavior still require per-source validation; compare representative rows against an independent venue/vendor and inspect market session semantics before using them in research.

## Subsequent 1,000-call daily-candle batch

The user then ran a 1,000-call batch on the same manifest. Manifest state after that run:

- **610 complete candle tasks**, **1 partial task**, **19,169 pending tasks** (3,632 candle tasks and 15,537 series tasks).
- **1,010 partitions**, **2,837,642 returned rows**, **10,328,113,351 bytes** on local disk (about 1.03 GB decimal).
- Independent streamed validation found **0 duplicate** `(dataset, symbol, timestamp)` keys, **0 basic OHLC range violations**, **0 JSON/number parse errors**, **0 missing timestamps**, and **0 file-vs-manifest row-count mismatches** across those partitions.
- Current provider `/usage` reported 3,468,452 bytes used in the month/week at run start, much lower than local JSONL size. Do not interpret that field as total local/network bytes until the provider defines its accounting scope. Continue to monitor both provider usage and actual disk usage.

At the 1,000-call checkpoint, processing was still in candle classes because those tasks precede series tasks in the manifest; series acquisition had not yet started at that checkpoint. This was a partial acquisition, not full coverage; preserve the SQLite manifest and run output to resume.

## Subsequent 10,000-call batch — state at interruption

The user ran with `--max-calls 10000`; after 1,672 requests the service returned HTTP 500 for `stocks/VCTR`, and the runner stopped with a checkpoint. Current local manifest and partition audit show:

- **11,566 complete tasks:** 4,226 1d candle instruments and 7,340 series instruments.
- **8,213 pending tasks:** 16 candle instruments and 8,197 series instruments.
- **1 blocked task:** `stocks/VCTR`, HTTP 500, no rows written. Normal reruns skip blocked tasks and proceed; `--retry-blocked` explicitly requeues a transient-status task.
- **Returned rows:** 9,538,465 candle rows and 4,754,936 series rows; **14,293,401 total** across 12,682 page files.
- **Local storage:** 4,955,177,437 bytes in JSONL partitions (~4.96 GB decimal).
- Full page audit verified every saved file's byte count and newline count against SQLite manifest counts, with zero file/manifest mismatches. This does not parse or semantically validate every JSON record; the 10-call sample has the deeper OHLC/schema checks. The 2026-10-18 preflight and reference-export queue were not rerun; all **692 reference partitions remain pending**, with zero Parquet exports.

Do not delete `acquisition_manifest.sqlite` or local partitions. Rerun the daily/series sync with the same paths to continue pending tasks; it will skip VCTR and begin with remaining tasks. Retry VCTR separately with `--retry-blocked` only after treating the 500 as transient or after the provider confirms the symbol is healthy.

## Resume procedure

Run the same `sync_lse_daily_and_series.py` command against the same catalog/preflight snapshot and output directory. It resumes pending tasks and pages already completed remain stored; do not delete the local SQLite manifest or JSONL partitions. Begin with modest batches and review usage/disk after each run.

## Remaining acquisition scope

- 4,237 daily-candle catalog tasks and 15,537 series tasks remain unprocessed at this pilot point.
- The separate reference-export manifest contains 692 partitions and is still pending. It consumes export jobs/bytes and should be processed in a distinct staged workflow; especially large options-flow tables need small size-tested partitions.
- The sampled SPY options chain remains a freshness blocker; see [[LSE bounded schema sample findings 2026-10-18]].

Related: [[LSE catalog coverage review 2026-10-18]] · [[Run LSE daily series sync]] · [[Exhaustive dataset inventory and transformation protocol]] · [[Data validation patterns]] · [[Data provenance and point-in-time]]
