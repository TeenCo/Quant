# Exhaustive Dataset Inventory and Transformation Protocol

This protocol turns a provider catalog into a reproducible inventory and then into validated, point-in-time research tables. “Exhaustive” means every source-listed dataset/instrument/time range is accounted for as acquired, unavailable, restricted, failed, or intentionally excluded—not that every available byte should be downloaded blindly.

## Current workspace status

- No market-data files (CSV, Parquet, spreadsheets, etc.) are present in the workspace as of the current inventory pass.
- The archived chat JSON is project context, not a market dataset.
- [[London Strategic Edge]] documents catalog/history/export methods, but catalog contents, access quota, data windows, schemas, and account entitlements must be read from the user's authorized account/API.
- The SDK license applies to client code; data licensing is separate. Its documented terms restrict redistribution/resale or making LSE data available to third parties. Do not copy credentials or restricted payloads into this Obsidian vault.

## Phase 1 — Capture the provider catalog

For every category/dataflow returned by the provider, record one inventory row per dataset × instrument × timeframe × available date span. Preserve the raw catalog response if the data terms allow it; otherwise save a compliant response hash, retrieval timestamp, endpoint/query, and schema summary.

### Inventory schema

| Field | Meaning |
|---|---|
| `source_id` | Stable provider/product identifier and version, if supplied. |
| `category` | Provider grouping, preserved verbatim. |
| `dataset_id` | Exact dataset/table/feed name. |
| `instrument_id` | Exact provider symbol plus independent stable mapping where available. |
| `market_type` | Spot, future, option, equity, ETF, macro series, reference data, etc. |
| `native_resolution` | Event/tick/bar/series frequency as documented and observed. |
| `first_available` / `last_available` | Catalog-declared bounds, not assumed complete bounds. |
| `first_observed` / `last_observed` | Bounds actually returned in validation/acquisition. |
| `timestamp_semantics` | Event, bar open/close, publication, settlement, or unknown; timezone and precision. |
| `schema_version` | Field list/types, units, identifier and null conventions. |
| `availability_class` | Point-in-time versioned, event archive, latest-history-only, adjusted/backfilled, or unknown. |
| `license_status` | Terms URL, intended use, retention, commercial use, derived data and redistribution status. |
| `access_status` | Accessible, requires entitlement, restricted, unavailable, not tested, or excluded. |
| `coverage_status` | Complete against contract/catalog expectation, partial, unknown, or failed. |
| `validation_status` | Not run, pass, warning, quarantine, or fail, with report reference. |
| `exclusion_reason` | Explicit rationale where not acquired or transformed. |
| `retrieved_at_utc` | Actual catalog/sample/acquisition time. |

Never fill account-dependent fields from provider marketing claims. Mark unverified values as `unknown` until observed.

## Phase 2 — Data acquisition in complete, auditable partitions

1. Resolve terms and intended use **before** downloading. Exclude any field/product whose license does not permit the research, storage, or transformations intended.
2. Freeze the inventory snapshot and define acquisition unit (dataset, instrument, timeframe, calendar interval) so completion can be counted.
3. Partition bounded date ranges according to endpoint limits; persist request parameters, page/cursor, status, byte/row counts, response hash if allowed, and errors.
4. Write each completed partition atomically. Incomplete exports stay marked partial; empty/error responses do not mean zero observations.
5. Use bounded retries/backoff and respect server quotas. Store credentials only in local environment/secrets management, never in notes, notebooks, logs, or manifests.
6. Resume from last committed partition after interruption and make the acquisition idempotent, avoiding duplicates.
7. Maintain a reconciliation table: listed expected partitions versus acquired/failed/restricted/unavailable partitions. “Complete” requires every expected partition to have a disposition.

## Phase 3 — Canonicalization without losing source meaning

Keep layers separate:

1. **Source response:** provider-native payload/file, immutable where license permits.
2. **Parsed table:** typed fields with source IDs and raw timestamp retained.
3. **Canonical observations:** normalized identifiers/units/timezones, preserving source-specific columns and version.
4. **Validated observations:** QC outcomes, exception flags, no silent deletion.
5. **Research features/labels:** separately versioned transforms with point-in-time cutoff and fitted parameters.

Never overwrite original rows with cleaned or adjusted versions. Every derived row must reference its source partition, transform version, parameters, and feature-ready time.

## Phase 4 — Exhaustive coverage and integrity checks

- Compare returned partition ranges, counts, identifiers and timeframes against the frozen catalog.
- Validate unique keys, pagination completion, schema changes, sequence continuity where applicable, and expected market calendars.
- For OHLCV, check interval boundaries, OHLC consistency, units, duplicate/missing bars, and current/incomplete-bar status. Gaps may reflect no trades or a feed outage; distinguish them.
- For quotes/trades/books, preserve venue, event time, receive time, sequence/trade ID, condition codes, and book-reset/gap state.
- For options/futures, validate contract identifiers, expiry, multiplier, adjustment, settlement and lifecycle status.
- For macro/reference series, preserve reference period, first publication time, vintage, correction flags, frequency and transformation.
- Compare representative periods to an independent source only when the definitions and venue/clock match. Record discrepancies rather than silently reconciling away differences.
- Report coverage by category, instrument, date, resolution, and validation state; include percent observed and explicit unknowns.

## Phase 5 — Point-in-time transformation

For each decision timestamp \(t\), use only observations whose source availability/receipt and transformation completion times are no later than \(t\). Keep `reference_time`, `published_at`, `received_at`, `processed_at`, and `valid_time` distinct. If provider history is revised or backfilled without preserved vintages, classify it latest-history-only and do not claim exact historical tradability.

Use [[Data provenance and point-in-time]], [[Data vintage and real-time testing]], [[Point-in-time feature availability contract]], [[Data contracts and lineage]], and [[API quotas retries and raw snapshots]] as detailed implementation references.

## Phase 6 — Coverage report and decision artifact

For each inventory snapshot, generate a machine-readable report and human summary containing:

- Number of listed/acquired/restricted/unavailable datasets and instruments.
- Date/timeframe/resolution coverage and holes by source.
- Schema/version changes and failed partitions.
- QC pass/warn/quarantine/fail rates and example exceptions.
- Point-in-time/vintage status and licensing status.
- Transform versions, output counts, lineage, and cost/storage footprint.
- Explicit exclusions and next acquisition/test decisions.

Only after the coverage report is reconciled should the data be used for cross-sectional discovery or model search. Exhaustive acquisition expands researcher degrees of freedom; maintain a trial ledger and pre-specify the first tests.

## LSE-specific next step

If the intended dataset is London Strategic Edge, use the user's local authorized API key to call the current catalog endpoints for each category, save the response according to provider terms, and populate the inventory schema above. First test one representative instrument per product type and verify history/export quotas. Do not share the key or data in this vault. The SDK examples in [[London Strategic Edge]] are illustrative and must be checked against the installed package version and current account catalog.

For a metadata-only first pass, follow [[Tools/Inventory LSE catalog]] and run the linked helper script. It prompts for the API key without echoing it, calls only `catalog()`, and writes a local JSON/CSV catalog snapshot with retrieval time and SDK version. The authorized 2026-10-18 catalog snapshot has been profiled; see [[LSE catalog coverage review 2026-10-18]]. The follow-up [[Tools/lse_metadata_preflight.py]] collects `vault_meta`, catalog, reference inventory and `/usage` metadata, still without requesting history, candles, options or live ticks. Keep outputs local under current provider terms; inspect catalog and quota before planning exports.

Once quota and metadata are available, [[Tools/build_lse_sample_plan.py]] can generate a local candidate review queue with up to three representative symbols per dataset and short date bounds. It makes no API requests. Review and curate that plan before any request; the dataset method hints may be unsupported for some dataset families.

The user's 2026-10-18 preflight succeeded; account limits and method availability are summarized in [[LSE catalog coverage review 2026-10-18]]. For the next schema check, use the opt-in [[Tools/Sample LSE endpoint schemas]] procedure. It caps per-call rows and explicitly avoids Parquet export jobs.

For the chosen acquisition scope (all cataloged **daily candles plus all series**), preview [[Tools/Run LSE daily series sync]]. Reference tables use a separate Parquet export queue in [[Tools/Plan and run LSE reference exports]] because those jobs have a five-per-hour limit and some inventories are very large. Both runners are resumable, user-confirmed, local-only operations; begin with small batches and stop at the configured byte safety reserves. These scripts do not claim data is complete or point-in-time correct merely because an endpoint returned rows.

## Research exercise

Take one source category and produce the catalog snapshot, reconciled inventory, acquisition partition ledger, QC report, and point-in-time classification. A correct result may show that the source cannot support a strict historical backtest; that is a useful research conclusion, not a failed deliverable.

Related: [[Research pipeline architecture]] · [[Experiment reproducibility]] · [[Data validation patterns]] · [[Data dictionary and provenance card]] · [[Source grading]] · [[Edge validation]]
