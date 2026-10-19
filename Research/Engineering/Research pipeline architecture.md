# Research Pipeline Architecture

This note proposes a practical structure for repeatable data research. It is provider-neutral; apply the requirements in [[Data provenance and point-in-time]] and the relevant source terms before building a production pipeline.

## Lifecycle

```text
source registry → acquisition → immutable raw snapshot → validation → canonical tables
               → point-in-time features/labels → experiment run → report/artifacts
```

### 1. Source registry

For each source, maintain an owner, dataset/product, endpoint, authentication method, rate limits, terms, native schema, timestamps, revisions, expected update schedule, and fallback. Keep secrets outside source control and vault notes.

### 2. Acquisition and raw snapshots

- Make requests reproducibly: explicit start/end, symbol, parameters, API/package version, retrieval time, and user agent where required.
- Save original responses/files unchanged; treat normalization as a separate downstream transformation.
- Use a source-specific idempotency key (source + instrument + range + query/version) to avoid duplicate pulls.
- Persist checksums and byte counts; do not overwrite an earlier snapshot when the provider corrects history.
- Handle pagination, retryable failures, rate limits, partial results, and API response errors explicitly.

### 3. Validation before transformation

Check schema and column types, primary-key uniqueness, timestamp ordering, gaps, duplicates, missing values, OHLC invariants, units, bounds, currency, and known feed/status codes. Save a machine-readable validation report; quarantine unexpected data rather than silently dropping it.

Schema validation can be implemented with explicit contracts (e.g. Pandera DataFrame schemas); these are engineering checks, not proof that a measurement is economically correct.

### 4. Canonical and derived layers

- Normalize identifiers and retain original provider identifiers.
- Normalize time representation while preserving original event/publication/receive timestamps and timezone.
- Maintain raw, cleaned, adjusted, feature, and label layers distinctly.
- Make each transform deterministic, versioned, and traceable to its inputs.
- Keep point-in-time joins separate from latest-history descriptive joins.

### 5. Experiment records

For every run, record a unique run ID, hypothesis, source/data snapshot IDs, git commit or code digest, environment/lockfile, config, random seed, sample/split boundaries, feature and label versions, costs, metrics, warnings, and output artifacts. Group related runs under an experiment but never remove null or failed trials.

Tools such as MLflow can track parameters, metrics, code versions, and artifacts. A tracking tool does not itself guarantee unbiased evaluation; split and data lineage must be designed by the researcher.

### 6. Reports and handoff

Each result should be re-creatable from its run manifest, and should include the source card, split definition, benchmark, uncertainty, net costs, regime breakdown, data limitations, tested variants, and next falsification. Link the report from the vault and append a timestamped entry to [[log]].

## Example project layout

```text
project/
  README.md                 # hypothesis, owner, data terms
  pyproject.toml            # environment and pinned dependencies
  configs/                  # run and data-source configuration; no secrets
  manifests/                # data/run metadata and checksums
  src/                      # acquisition, validation, transforms, models
  tests/                    # schema, time, mapping, and leakage invariants
  data/raw/                  # immutable or object-store-backed snapshots
  data/processed/            # deterministic canonical tables/features
  reports/                   # run summaries, plots, and decisions
```

For large datasets, keep bulky data out of ordinary Git history; use an approved object store or a data-versioning system such as DVC, and version the pointer/manifest. Keep credentials in ignored local configuration or a secrets manager.

## Failure policy

- Never treat empty response, API error JSON, rate-limit response, or stale cache as valid zero observations.
- Mark partial downloads and record the missing ranges before resuming.
- Pin schema assumptions and fail visibly on unexpected columns/types.
- Log retries, request IDs, source status, counts, and error classes; exclude credentials and sensitive payloads from logs.
- Preserve raw input before attempting repair. Record any repair as a derived transformation.

## Idempotency and recovery example

For a paginated daily feed, define a partition key (provider, product, instrument, date range, query version) and a deterministic page/cursor record. Write each page to a temporary object, validate response status/schema and expected cursor progression, then atomically commit it with row count/checksum/status. On retry, resume from the last committed cursor; do not append the same page twice. A missing page is an incomplete partition, not an empty period.

## Data contracts at stage boundaries

Each pipeline boundary should state schema, primary key, sort order, timestamp/availability semantics, unit/currency, null policy, and invariants. Validate contract before and after transformations. Preserve quarantine rows and exception disposition, since silent “cleaning” can selectively remove crashes, illiquid instruments, or failed issuers.

## Reproducibility versus reproducible access

If raw data cannot be retained under terms, the run may not be snapshot-reproducible. Preserve compliant query metadata, source version, retrieval timestamp, field dictionary, license reference, response hash if permitted, and a concise note that re-query may return revised data. State the attained reproducibility level using [[Experiment reproducibility]].

## Connected notes

[[Research pipelines]] · [[Data provenance and point-in-time]] · [[Data vintage and real-time testing]] · [[Performance]] · [[Research workflow]] · [[Data dictionary and provenance card]] · [[API quotas retries and raw snapshots]] · [[Data contracts and lineage]] · [[Schema domain temporal validation]] · [[Manifests tracking security and licensing]]
