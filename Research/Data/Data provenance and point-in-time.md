# Data Provenance and Point-in-Time Integrity

## Why this matters

A historical observation is not automatically a record of what a researcher could have known at the time. A dataset may have been revised, backfilled, adjusted, remapped to modern identifiers, or corrected without preserving prior versions. These choices can create look-ahead, survivorship, and measurement bias even when the raw values are accurate today.

## Two clocks for every datum

For each observation, distinguish at least:

- **Reference/event time:** when the economic activity or market event occurred.
- **Publication/availability time:** when a decision-maker could first access the value.

For operational data, also record ingestion time, vendor time, exchange sequence, and local receipt time as relevant. Never silently substitute reference time for publication time.

## Provenance record

Every dataset or major field should have a data card recording:

| Field | What to capture |
|---|---|
| Source | Publisher, product, endpoint/file, contact or documentation link. |
| Claim grade | Evidence grade for data-access/coverage claims (see [[Source grading]]). |
| Identifier | Original key, ticker/CIK/ISIN/contract code/station ID, mapping history. |
| Scope | Universe, geography, venues, markets, entities included/excluded. |
| Time semantics | Reference, publication, event, receipt times; timezone; precision; trading calendar. |
| Revisions | Vintage/real-time history available? Correction policy? Backfill and corporate-action policy? |
| Frequency | Native granularity, aggregation window, bar timestamp convention. |
| Completeness | Start/end span, missing periods, coverage changes, minimum-reporting thresholds. |
| Transformations | Raw vs adjusted, units, seasonal adjustment, currency, roll, deflation, aggregation. |
| Licensing | Research, commercial use, storage, retention, and redistribution rights. |
| Retrieval | Query, parameters, retrieval time, package version, schema, checksum if allowed. |
| Validation | Cross-source checks, gaps/duplicates, known caveats, quality results. |

## Revision and vintage design

1. For revised data, preserve the original release and each subsequent vintage when available.
2. Store the reference period and release timestamp separately.
3. Build backtests by joining each decision to the latest vintage publicly available by that decision time.
4. Preserve release calendars and revisions; do not use final values as if published initially.
5. If vintage history is unavailable, mark the field as **not point-in-time verified** and either exclude it from strict historical tests or bound its potential effect.

FRED's observation API supports real-time periods and `vintage_dates`; ALFRED provides dated vintages. This is a strong pattern for macro series, though each series still has its own release/revision semantics.

## Identifier and universe hygiene

- Prefer stable entity identifiers (CIK, LEI, FIGI/ISIN where licensed) over ticker strings alone.
- Keep dated ticker/name/venue mappings; tickers can be reused, changed, or delisted.
- Track historical constituents, mergers, spin-offs, bankruptcies, suspensions, and product expirations.
- Distinguish a modern continuous/adjusted series from individual historical contracts or securities.
- Record whether the publisher's coverage universe is survivorship-biased or begins only after liquidity/listing screens.

## Corrections are not the same as vintages

A source may show a corrected latest historical file but not preserve the superseded value. A current history that has been corrected is better for descriptive analysis; without the old values and correction timestamps, it cannot establish what was known in a historical simulation. Label these separately:

- **Vintage-aware:** prior versions can be reconstructed by date.
- **Latest-history only:** current values overwrite prior releases/corrections.
- **Unknown:** revision behavior has not been documented or tested.

## Quality-control gates

- Schema/type/unit consistency and explicit missing-value codes.
- Unique key and timestamp checks, sequence gaps, duplicates, and clock monotonicity.
- Coverage counts by instrument, date, region, venue, and source vintage.
- Impossible values, jumps, price adjustment consistency, corporate-action reconciliation.
- Cross-check against another source or official release where feasible.
- Explicit status flags for preliminary, revised, estimated, suppressed, or stale observations.

## As-of join example

Suppose an observation has `reference_period=2025-01`, initial `published_at=2025-02-12 08:30 ET`, and a revision published on 2025-03-14. For a decision at 2025-02-20, join the initial vintage; for a decision before 08:30 ET on February 12, do not use it. For a March 20 decision, use the revision only if the research question models the revised value becoming available then. The valid join key is not simply reference month: retain a version table ordered by publication/availability timestamp and select the latest eligible version at each decision time.

In SQL-like terms, candidates satisfy `published_at <= decision_time`; choose the row with maximum `published_at` per series/reference period, then apply the declared release/aggregation rule. If the source overwrites revisions, the historical as-of join cannot be reconstructed exactly and must be labeled accordingly.

## Data lineage and reproducible transformations

Treat every derived field as a directed lineage graph: source record/version → parsing → unit/time normalization → entity mapping → cleaning → feature aggregation. Keep code version, parameters, and upstream identifiers so a result can be traced back to input records. Raw snapshots may be immutable only when licensing permits retention; otherwise store compliant query metadata/checksums and document that the source may no longer reproduce the exact response.

Use separate status labels for provider claims, independently sampled validation, and research suitability. “Official,” “complete,” “real-time,” and “free” are distinct claims. Test access from a small sample and inspect terms before scaling or redistributing.

## Connected notes

[[Market data]] · [[Feature engineering]] · [[Alternative-data research design]] · [[Research pipelines]] · [[Financial data source directory]] · [[Source grading]] · [[Bitemporal versioned joins]] · [[Identifier and security master lifecycle]] · [[API quotas retries and raw snapshots]]
