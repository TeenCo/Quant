# Market Data: Structure, Provenance, and Pitfalls

Market data is an observation process, not the market itself. Data quality, sampling, and timestamps can create apparent patterns or erase real ones.

## Data classes

- Trades, quotes, order books, and exchange events.
- OHLCV bars at multiple resolutions.
- Corporate actions, dividends, splits, symbol mappings, and point-in-time universe membership.
- Options chains, trades, implied volatility, and greeks.
- Futures contracts, expiries, rolls, and positioning.
- Macro series, releases, revisions, calendars, and yield curves.
- Alternative observations (web, shipping, imagery, text, payments, sensors, etc.).

## Minimum provenance record

Provider and source; license and permitted use; instrument/venue; event and publication time; timezone/clock convention; frequency/resolution; adjustments and transformation; coverage start/end; missingness; revisions; symbol mapping; survivorship; quality checks; download/query date and reproducible identifier.

## Research hazards

- Look-ahead from bars stamped at their close, late-arriving trades, revisions, or future universe constituents.
- Survivorship, delisting, backfill, and selection of liquid/available instruments.
- Exchange timezone, daylight saving, holidays, stale marks, asynchronous markets, and duplicate/missing records.
- Vendor-specific aggregation, price adjustment, FX volume representation, tick filtering, and symbol mapping.
- Data snooping across many providers, frequencies, and transformations.
- Licensing restrictions on storage, derived data, redistribution, and commercial use.

## Quality checks

Check row counts and expected sessions, monotonic/unique timestamps, OHLC consistency, impossible returns, duplicate events, missing intervals, cross-source price overlap, corporate-action effects, and coverage by asset/time. Keep validation results and raw data separate from cleaned outputs.

Use [[Data provenance and point-in-time]] to record the evidence and lineage of every field, [[Data vintage and real-time testing]] for revised series, and [[Survivorship, identifiers and universe]] for historical membership and security lifecycle handling. The reusable [[Data dictionary and provenance card]] captures these fields.

Related: [[London Strategic Edge]], [[Feature engineering]], [[Forex]], [[ETFs]], [[Crypto]], [[Equities]], [[Futures]], [[Options]], [[Fixed income]], [[Commodities]].
