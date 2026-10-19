# LSE Bounded Schema Sample Findings — 2026-10-18

This note records a user-authorized, local, bounded endpoint sample from LSE SDK 0.14.0. It characterizes selected response structures only; it is not a completeness, accuracy, or point-in-time validation of the full catalog.

## Provenance and request scope

- **Catalog:** `lse_catalog_20261018T135141Z.json`, 22,966 catalog rows.
- **Preflight:** `lse_metadata_preflight_20261018T135558Z.json`.
- **Sample artifact:** `lse_bounded_endpoint_samples_20261018T140151Z.json` (local under the user's private `lse_catalog_snapshot/bounded_samples` folder; not in this vault).
- **SDK:** 0.14.0.
- **Requests:** 29 bounded endpoint calls, each capped at no more than 3 returned rows. 29 succeeded, 0 returned errors. No `history()`, `dataset()`, or WebSocket stream call was made; no bulk export job was launched.
- **Permissions:** user authorized processing the sample artifact. Retain it locally under current LSE terms; do not redistribute rows or place raw samples in a shared repository.

## Observed schema families

| Family | Example fields observed | Clock shape | Notes |
|---|---|---|---|
| Daily candles (10 class samples) | `symbol`, `open`, `high`, `low`, `close`, `volume`, `timestamp` | ISO string with `Z`; daily bar timestamps at 00:00Z in sample | 36 returned OHLC rows passed basic `low <= open/close <= high` validation. Volume types varied (integer/float), and FX volume semantics need vendor clarification. |
| Series (7 class samples) | `date`, `symbol`, `value` | Date-only; no intraday availability clock | Series values require unit, source, frequency, revision and release-time metadata not present in this response shape. |
| Options chain | OSI `ticker`, underlying, strike, expiry, contract type, price, volume/premium, IV/Greeks, DTE, `last_trade_at`, `updated_at` | event/update timestamps available per row | **Critical sample anomaly below:** returned contracts were stale/expired relative to sample retrieval time, and DTE values disagreed with expiry and current date. |
| Options flow | `id`, `ts`, contract/underlying, premium, volume, IV/Greeks | UTC-like timestamp string | The three sample prints were timestamped 2026-10-16, consistent with the last catalog date, but this alone does not establish coverage or completeness. |
| Option 1-minute bars | `ticker`, `minute`, OHLC, volume, premium, print count, averaged Greeks | minute timestamp string | Sample rows were from 2026-06-17 for the selected contract; contract history coverage is contract-specific. |
| Reference tables | schema depends on table (e.g. COT release/date/positions; financial reports include nested `data`; events include date/time/actual/consensus) | mixture of date-only, date/time, accepted/update times | Do not force a single canonical timestamp or schema across these tables. Preserve table-specific observation and publication semantics. |

## Critical options-chain staleness/DTE finding

The `options()` chain request for `SPY` with `max_dte=30` returned three `SPY260702...` contracts expiring **2026-07-02**, while the sample was retrieved at **2026-10-18T14:01:51Z**. The rows' `last_trade_at`/`updated_at` were 2026-06-17, 2026-06-26, and 2026-07-01. Their reported DTE values were 15, 6, and 1, respectively—values tied to historical snapshots and not the retrieval date. All three contracts had already expired by retrieval date, so the `max_dte=30` filter did not guarantee a current chain in this observed response.

**Disposition:** Do not use this chain endpoint as a current/point-in-time chain without investigating server semantics. For any option research, require `updated_at`/`last_trade_at` freshness checks, compute DTE independently from expiry and the intended decision timestamp, reject expired/stale quotes, verify the chain is current, and compare a bounded contract sample against a licensed independent source or exchange data. Record this as a blocking feed-quality issue for chain-based use until resolved. The separate `options_flow` sample was recent; it does not validate chain freshness.

## QC summary

- All 36 sampled OHLC rows passed simple bar bounds checks. This is a syntax/domain check only, not price accuracy validation.
- Sample calls returned 14 distinct field-name schemas, highlighting why a single generic parser is unsuitable.
- One `stock_splits` call returned zero rows for AAPL over the one-year sample window; that is plausible for this query and is not treated as an endpoint failure.
- Some profile/fundamental methods returned one row despite a limit of three; returned row count is not expected to equal the cap.
- Catalog timestamps and series dates still require provider-specific definitions, release/publication clocks, and point-in-time treatment.

## Bounded sample transformation prototype

The 80 returned rows were normalized locally with [[Tools/normalize_lse_bounded_samples.py]] into `lse_sample_canonical_rows.csv`, accompanied by `lse_sample_transform_manifest.json`. Both outputs are in the user's private `lse_catalog_snapshot/bounded_samples/transformed_samples` directory, not this vault. The prototype adds endpoint/family, source retrieval time, row index/key, instrument/underlying/contract, timestamp field/value/semantics, and common OHLC/series fields while retaining the full original row in `raw_record_json`.

No units were converted, timestamps reinterpreted, records deduplicated, or gaps filled. Manifest QC flagged all three option-chain rows as expired at sample retrieval; 36 OHLC rows passed simple bounds. The prototype demonstrates lineage and schema-preserving normalization only; it does not supply a production canonical model or validate the complete underlying datasets.

## Next actions before transformations

1. Contact/consult current LSE API documentation for the observed `options()` freshness/DTE behavior; repeat only a small bounded query after the issue is explained.
2. Validate one representative observation per selected family independently (or against an official source where comparable).
3. Add transformation-specific schemas keyed by dataset/method, with field units, null rules, timestamps, identifiers, and version.
4. Keep latest-history-only series separate from executable bar/event tables; define availability before backtesting.
5. Only then prioritize and export bounded historical partitions, reconciling each partition and using account usage limits.

Related: [[Exhaustive dataset inventory and transformation protocol]] · [[LSE catalog coverage review 2026-10-18]] · [[Options]] · [[Volatility surface Greeks and event variance]] · [[Data provenance and point-in-time]] · [[Data validation patterns]] · [[Edge validation]]
