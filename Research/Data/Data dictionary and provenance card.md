# Data Dictionary and Provenance Card

Copy this template into a dataset note before using new data.

Use one card per source product and one field-level dictionary for consequential variables. Preserve the distinction between a source's own description and empirical validation of its completeness, latency, and stability.

## Identity

- Dataset / table / series name:
- Publisher / vendor:
- Official documentation and landing page:
- API endpoint / file product / query:
- Data source grade (1 strongest–10 weakest):
- Access: public / key / subscription / institutional agreement / restricted:
- License / terms / commercial use / redistribution:
- Retrieval date/time and timezone:
- SDK / schema / version:

## Universe and identifiers

- Instruments/entities/stations and universe definition:
- Stable identifiers:
- Symbol/entity mapping source and history:
- Delisted, merged, inactive, or missing entities retained?
- Venue, geography, reporting population:

## Time semantics

- Event/reference time:
- First-public/availability timestamp:
- Vendor ingestion / receipt timestamp:
- Timezone and daylight-saving policy:
- Frequency / event granularity:
- Timestamp meaning (bar open/close, transaction, release, settlement):
- Trading/event calendar:

## Revisions and transformations

- Vintage history available? How retrieved?
- Correction policy and whether prior values are preserved:
- Preliminary/final/estimated/suppressed indicators:
- Corporate-action, roll, seasonal, inflation, currency, or benchmark adjustments:
- Native units and transformation formulas:
- Known methodology breaks and date ranges:

## Quality audit

- Coverage start/end and count by period:
- Missing intervals / duplicate keys / invalid values:
- Cross-source validation and discrepancies:
- Suspected survivorship, backfill, or stale-data risks:
- Quality tests performed and results:

## Research use

- Hypothesis / target field:
- Point-in-time join logic:
- Known limitation for backtests:
- Derived data/cache location and checksum if permitted:
- Follow-up / owner:

## Example: event and availability clocks

| Field | Meaning | Example |
|---|---|---|
| `event_time` | When source event occurred | 2025-02-12 08:30:00 America/New_York |
| `published_at` | First public release time | 2025-02-12 08:30:00 America/New_York |
| `received_at` | When collector received it | 2025-02-12 08:30:02 UTC |
| `reference_period` | Period described by value | 2025-01 |
| `vintage_id` | Version/release identifier | release-2025-02-12 |

For a trading simulation, define the earliest usable time from the actual observable/received/processed clock and any required cleaning latency, not from a backdated reference period. Record timezone and daylight-saving conversion explicitly.

## Example QC rule

For a daily OHLC series, assert unique `(instrument_id, session_date)` keys, `low <= min(open, close)`, `high >= max(open, close)`, positive prices where required, and valid exchange sessions. A failed condition should route to a quarantine/exception report with raw values preserved; do not silently drop the row. The precise rules depend on instrument conventions (negative futures prices are possible in some markets), so make checks market-aware.
