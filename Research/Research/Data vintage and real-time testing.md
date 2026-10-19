# Data Vintages and Real-Time Backtesting

## The core timing test

For a feature used at decision time `t`, ask: **could the value and its exact version have been retrieved by a participant at time `t`?** A historical reference period does not answer this. Record first publication time, data vintage, ingestion latency, and the time at which your system could actually use it.

## Vintage categories

- **True real-time/vintage history:** prior releases or states are separately retained with availability timestamps.
- **Event archive:** source records and their publication/arrival times can be reconstructed (e.g. SEC filings with accession/acceptance metadata).
- **Latest historical snapshot:** past observations are replaced by corrections/revisions; old values may be unrecoverable.
- **Retrospectively adjusted:** prices or membership are normalized using later corporate actions or current constituents.
- **Unknown:** source has not documented or exposed revision timing.

Record the category per field; do not assume an entire provider has a single revision behavior.

## Vintage-aware construction

1. Save each source release or snapshot with a retrieval timestamp and immutable checksum where permitted.
2. Preserve `reference_period`, `published_at`, `received_at`, `valid_from`, and `valid_to` when meaningful.
3. For every historical decision, join only values whose availability timestamp is no later than the decision time.
4. When a later revision arrives, append a new version; do not overwrite the old value in the point-in-time store.
5. Test same-day decisions with realistic release clock and processing latency. A date-only join is often insufficient.
6. Separately test final revised values for descriptive analysis, labeling them as hindsight/revised.

## A vintage-aware example

Suppose an economic series has observation reference month `m`, first value published at `p1`, and revisions at `p2`, `p3`. A strategy decision `t` may use `p1` if `p1 <= t`; if `t < p1`, it cannot use the value even though month `m` has ended. If the study uses the latest value at `t0` for all historical `t`, it can leak revision information.

FRED observation queries support real-time periods and `vintage_dates`, while BLS reports can include preliminary footnotes and revisions. SEC filing APIs update as filings are disseminated and contain filing/acceptance metadata. Check the specific series or tag's release and correction policy.

## Bitemporal storage pattern

Where records can be corrected or reclassified, keep both **valid time** (when the fact applies in the world) and **transaction/availability time** (when the database/source made that version visible). A row can be modeled as `(entity, fact, value, valid_from, valid_to, published_at, superseded_at, source_version)`. Historical decisions query the version with `published_at <= decision_time`; descriptive studies may query the latest version. Never overwrite the old value if the source and license allow preservation.

## Same-day event ordering

If a source says “released on date D” but provides no time, do not assume availability at the market open. Use the earliest defensible release-time interval and test conservative lags (for example, next session) until exact timing is verified. Date-only joins can create look-ahead around after-hours and intraday announcements. Record exchange timezone, daylight-saving rules, and whether a release coincided with a halt/closure.

## When vintage data are missing

- Exclude the feature from confirmatory historical backtests or classify it as an exploratory upper-bound study.
- Bound the uncertainty with release-lag assumptions, revision-size analysis, or a genuinely real-time subperiod.
- Avoid asserting the estimated performance was historically achievable.
- Seek an alternate source with preserved releases; document source differences.

## Connected notes

[[Data provenance and point-in-time]] · [[Feature engineering]] · [[Research workflow]] · [[Statistical inference for trading]] · [[Market data]] · [[Financial data source directory]]
