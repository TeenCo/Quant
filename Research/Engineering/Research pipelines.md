# Reproducible Research Pipelines

A pipeline makes data acquisition, transformation, modeling, evaluation, and reporting repeatable and auditable.

For a more detailed stage-by-stage architecture, see [[Research pipeline architecture]]. For run manifests and reproducibility levels, see [[Experiment reproducibility]].

## Suggested layers

1. **Source/raw:** immutable provider response or file, retrieval metadata, license, checksum where allowed.
2. **Validated:** schema and quality checks, normalized timestamps, symbol mapping, point-in-time fields.
3. **Features/labels:** deterministic transformations with versioned definitions and strict time semantics.
4. **Experiments:** config-driven training/backtests; isolated splits; trial ledger; environment and seed record.
5. **Results:** metrics, plots, sensitivity analysis, decision-cost assumptions, and full caveats.
6. **Monitoring:** drift, data freshness, execution, cost, and out-of-sample performance.

## Engineering principles

- Separate raw from derived data; make transformations idempotent where possible.
- Use explicit schemas, stable IDs, UTC/event-time policy, and data-vintage versioning.
- Test invariants such as chronological order, no duplicate keys, valid OHLC, and no future join.
- Cache only with complete input/code/config version keys.
- Make jobs restartable and resource-aware; log failures and quotas.
- Keep secrets out of notebooks, source control, and the Obsidian vault.
- Record package versions, hardware, random seeds, and run timestamps.
- Validate structural and domain-specific invariants at each handoff; see [[Data validation patterns]].

See [[Performance]], [[Market data]], [[London Strategic Edge]], and [[Research workflow]].
