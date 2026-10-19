# Experiment Tracking: Implementation Notes

The tracking layer should make trial search visible and results comparable. A local file-based setup can work for a solo prototype; a shared backend/artifact store is a team infrastructure decision requiring access controls and approved storage.

## Log for every run

- Hypothesis and registered primary evaluation.
- All data source IDs, snapshots, query parameters, time/vintage policy, and dataset hash/reference.
- Code commit/digest, dependency lock, hardware/runtime, and random seed.
- Universe, features, labels, sample boundaries, fold construction, and any purge/embargo.
- Model parameters, fit status, warnings, and tuning/search decisions.
- Gross and net metrics, uncertainty estimates, transaction-cost assumptions, turnover, exposure, and capacity metrics.
- Diagnostics, plots, validation errors, and null outcomes.

## Tool options

- **MLflow Tracking:** records runs, params, metrics, code versions, data references, and artifacts; defaults can be local and support backend/artifact stores.
- **DVC:** versions pointers to large data/model files and supports remote storage, while code/metadata can remain in Git. Configure credentials outside tracked files.
- **Git + lockfiles:** version code and dependencies; does not version external data by itself.
- **Frictionless Data Package:** a lightweight descriptor for packaging resource locations, sources, license metadata, and schema references.

Pick tools only after clarifying storage policy, access control, dataset rights, and operational needs. A tool can faithfully track a flawed or leaked experiment.

## Minimal run protocol

1. Create a run ID and immutable config before execution.
2. Validate data and write the data card/snapshot reference.
3. Execute train/validation/test exactly as specified; no interactive changes to the final holdout.
4. Log metrics and artifacts automatically; save stdout/stderr and exceptions.
5. Compare with baselines and prior trials, not only the best run.
6. Generate a human-readable report; append an ISO timestamped note to [[log]].

See [[Experiment reproducibility]] and [[Research pipeline architecture]].

## Trial taxonomy

Tag runs as feasibility, exploratory, confirmatory, robustness, or production-monitoring. Record the parent hypothesis and whether the run's results were viewed before subsequent design choices. A run name is not a statistical family definition; maintain explicit relationships among variants, including feature/label, universe, cost, and sample-window changes.

## Minimal schema and comparisons

Use stable fields for run ID, parent experiment, status, code/data version, split, target, metric, uncertainty method, cost model, and artifacts. Compare models only on common forecast origins and same target definitions; preserve per-origin predictions so paired loss tests and calibration can be revisited. Dashboards should show all runs and allow null/failed filters rather than sorting only by headline Sharpe.

## Access and retention

Before choosing a tracking backend, confirm access control, restricted-data handling, retention, export, and backup policies. Never send proprietary raw data or secrets to an unapproved artifact store. Tracking tools improve auditability only if their logged parameters and data references are complete and accurate.
