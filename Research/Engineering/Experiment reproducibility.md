# Experiment Reproducibility and Audit Trail

Reproducibility means an independent researcher can reconstruct what was run, on which data version, using which code, parameters, and validation design—and can determine what the result does and does not establish.

## Run manifest fields

```yaml
run_id: unique-id
created_at_utc: timestamp
hypothesis_id: link-or-id
code_revision: commit-or-digest
environment: lockfile-or-container-digest
data_sources:
  - source: provider/product/endpoint
    query: redacted-query-parameters
    retrieved_at_utc: timestamp
    snapshot_id: immutable-version-or-hash
    license_reference: source-terms-link
sample:
  universe_version: identifier
  start: YYYY-MM-DD
  end: YYYY-MM-DD
  feature_cutoff: timestamp-rule
validation:
  design: walk-forward/purged/etc
  folds: list-or-specification
  final_holdout_policy: description
model:
  class: model-or-rule
  parameters: explicit-values
  seed: integer-or-not-applicable
execution:
  benchmark: decision-price-definition
  fees_spread_impact_latency: assumptions
results:
  metrics: names-and-values
  uncertainty: method-and-values
  artifacts: paths
limitations: list
```

Do not place API keys, credentials, personally identifying data, or restricted raw data in the vault or a manifest committed to a shared repository. Store secret references, not secret values.

## Reproducibility levels

1. **Narrative:** a human-readable report explains the idea, but exact inputs/configuration may be missing.
2. **Scripted:** code and parameters can rerun against the same source, but source history may have changed.
3. **Snapshot-pinned:** inputs are versioned/hashed where terms permit; code and environment are recorded.
4. **Point-in-time reproducible:** vintage data, release/arrival clocks, historical universe, and decision cutoffs are reconstructable.
5. **Prospective:** the method is locked before new observations arrive and results are recorded prospectively.

Research claims should state which level was achieved. Prospective testing does not automatically imply broad external validity.

## Determinism and numerical reproducibility

Exact bitwise reproduction may be impossible across hardware, BLAS libraries, GPU kernels, parallel reduction order, or nondeterministic algorithms. State whether the goal is bitwise identity, metric agreement within a tolerance, or conceptual replication. Record package/runtime/hardware, deterministic settings, seeds, and tolerances. A seed alone does not guarantee repeatability when code, library versions, data ordering, or distributed execution differ.

## Artifact and report contract

Keep a compact report with hypothesis, estimand, source/vintage, universe, split and selection protocol, baseline, net-cost assumptions, uncertainty, results by time/regime, diagnostics, limitations, and next falsification. Link tables/plots to their run ID and data/code digest; do not publish screenshots without the underlying computation metadata. Preserve negative and failed runs as part of the reproducibility record.

## Experiment tracking tools

MLflow Tracking, DVC, Git, dependency lockfiles, and data-package descriptors can help record code/data/metrics/artifacts. They are optional implementations, not substitutes for a clear hypothesis, source permissions, timestamp logic, trial accounting, and methodological review.

## Reproducibility checklist

- [ ] Exact source/product, query, and terms recorded.
- [ ] Immutable raw snapshot or a documented reason it cannot be retained.
- [ ] Data dictionary, schema, source time semantics, and validation results saved.
- [ ] Code revision and dependencies pinned.
- [ ] Universe, feature/label definitions, costs, splits, and model parameters specified.
- [ ] All trials, including failed/null runs, preserved.
- [ ] Output metrics/artifacts and limitations linked to the run.
- [ ] Re-run or independent reproduction checked where possible.

Related: [[Research pipeline architecture]], [[Research pipelines]], [[Overfitting controls]], [[Data provenance and point-in-time]], [[Research workflow]], [[Manifests tracking security and licensing]], [[Data contracts and lineage]].
