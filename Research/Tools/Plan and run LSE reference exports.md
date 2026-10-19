# Plan and Run LSE Reference Exports

This guide covers [[lse_reference_export_queue.py]]. It creates a SQLite queue from the account's `reference_inventory` and partitions date-bearing datasets by day/month/year according to provider row-count metadata. This is a queueing heuristic only; estimates are not file sizes or completeness guarantees.

## Preview the queue

```powershell
python "Research\Tools\lse_reference_export_queue.py" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\preflight\lse_metadata_preflight_20261018T135558Z.json" `
  --out "C:\Users\Dell\Desktop\Quant\lse_reference_exports"
```

The preview makes no API requests and creates `reference_export_manifest.sqlite`. Current preflight produces 692 tasks: 401 daily (mostly options flow/1m), 5 monthly (options chain), 284 annual, and 2 undated snapshots. On execution the queue starts with the smallest row-count estimates to measure actual Parquet sizes before large partitions.

## Execute carefully

```powershell
python "Research\Tools\lse_reference_export_queue.py" `
  "C:\Users\Dell\Desktop\Quant\lse_catalog_snapshot\preflight\lse_metadata_preflight_20261018T135558Z.json" `
  --out "C:\Users\Dell\Desktop\Quant\lse_reference_exports" `
  --execute --max-jobs 1
```

It requires typing `EXPORT REFERENCE PARTITIONS`, prompts for the key invisibly, checks current `/usage`, and runs no more than the requested number of jobs or the remaining hourly allowance, whichever is lower. It preserves the Parquet files locally and records output paths/bytes/status in SQLite. It checks quota reserves before and after jobs, but a file's final size is unknown before export; keep `--max-jobs 1` for the first run to learn actual file size. Later, run up to the provider's remaining hourly allowance (maximum 5) if output sizes and byte headroom are known. If job/byte allowance is near the reserve, stop and wait for reset rather than retrying.

## Caveats

- Current preflight reports 0/5 hourly export jobs at its timestamp, 15 GiB weekly and 50 GiB monthly caps, 200 calls/minute, 5,000 row synchronous cap, and concurrency 2. Recheck live usage before each run.
- Options flow/1m inventory counts are hundreds of millions of rows; even daily partitions may be large. Consider prioritizing only after a first permitted small date partition establishes size and schema.
- The queue is deliberately separate from candle/series REST pagination. Each downloaded product has different field/time semantics and rights.
- Files contain LSE data. Keep the destination private and follow current terms; do not commit Parquet files to Git or place them in the Obsidian vault.

Related: [[LSE catalog coverage review 2026-10-18]] · [[Exhaustive dataset inventory and transformation protocol]] · [[Experiment reproducibility]] · [[Data provenance and point-in-time]]
