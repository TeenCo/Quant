# Quantitative Research Workflow

The goal is not merely to fit a predictor. It is to determine whether information available at the time could have supported a repeatable, tradable decision after uncertainty and implementation costs.

## 1. Frame a falsifiable question

Write a concise hypothesis before running broad searches. Define the asset universe, decision time, feature availability, forecast/holding horizon, target, action, and what observation would falsify the idea. Record the mechanism separately from the empirical prediction.

## 2. Establish data lineage

For each input record provider, collection time, event time, timezone, revision/vintage policy, transformations, coverage, license, and missing data. Confirm that values were actually available at the simulated decision time. Keep raw data immutable and derived data reproducible.

Use [[Data dictionary and provenance card]] as the minimum capture template and [[Data vintage and real-time testing]] for revision-sensitive data.

## 3. Define the estimand and baseline

Choose an outcome that maps to the proposed decision (e.g. future return net of expected costs, risk-adjusted return, execution shortfall). Specify simple baselines and no-trade or benchmark alternatives. Avoid selecting a target because it makes the current sample look favorable.

## 4. Design validation before fitting

Use chronological, point-in-time splits. For dependent financial observations, use purging/embargo or other dependence-aware methods where label windows overlap. Keep a final untouched period or use a pre-registered walk-forward design. Decide how hyperparameters and features will be selected without touching the final test.

## 5. Build a transparent baseline first

Start with simple rules, regularized linear models, or economically interpretable estimates. Inspect feature distributions, missingness, stability, residuals, and performance by time/regime/asset. Add complexity only when it demonstrates repeatable incremental value.

## 6. Control search and estimation bias

Track all trials, feature families, parameter choices, discarded variants, and stopping decisions. Use multiple-testing-aware inference and robust uncertainty estimates. Account for serial correlation, heteroskedasticity, overlapping returns, and selection. See [[Overfitting controls]].

## 7. Convert scores to decisions

Map forecasts into positions under explicit constraints, capital, turnover, leverage, borrow, exposure, execution delay, spreads, fees, impact, and financing. Do not confuse predictive accuracy with profitable implementability.

## 8. Stress and replicate

Test alternate reasonable data definitions, samples, costs, lags, universes, and related markets. Use event studies or placebo tests when appropriate. Seek independent data replication and a plausible explanation. Be alert to data snooping and regime dependence.

## 9. Measure degradation

Evaluate performance in rolling out-of-sample periods and by liquidity, capacity, volatility, and crowding proxies. Monitor feature/target drift, execution costs, decay from discovery to deployment, and whether the edge is simply a disguised known factor.

## 10. Publish the result, including nulls

Store code/version, data snapshot or source query, environment, run configuration, metrics, plots, all limitations, and next steps. Keep successful and failed research visible. Update [[log]] and link the finding to relevant [[Markets/Market data|data]], [[Market microstructure|market structure]], and market notes.

## Decision gates and stop rules

At each stage, define what must be true to continue:

- **Data gate:** source rights, coverage, time semantics, and validation are sufficient for the stated estimand.
- **Signal gate:** pre-specified predictive effect exceeds a meaningful baseline with uncertainty that accounts for dependence/search.
- **Robustness gate:** result survives plausible definitions, periods, instruments, and independent confirmation without requiring endless parameter rescue.
- **Implementation gate:** net expected value remains meaningful under realistic fills, cost uncertainty, capacity, and constraints.
- **Monitoring gate:** decay/drift alarms and retraining rules are fixed before new outcomes arrive.

Stop or downgrade when a required condition fails; retain the result as a null/limitation rather than repeatedly changing definitions until it passes. A failed data gate should prevent statistical claims about the intended market opportunity.

## Final memo structure

1. Hypothesis/mechanism and falsifying observation.
2. Data sources, permissions, provenance, and point-in-time status.
3. Estimand, universe, baseline, and frozen decision rule.
4. Validation, dependence, multiplicity, and selection procedure.
5. Predictive effect with interval and full trial context.
6. Net implementation, capacity, tail risk, and regime sensitivity.
7. Replication status, evidence grade, unresolved limitations, and next action.

For inferential details, use [[Statistical inference for trading]]; for unusual raw data, use [[Alternative-data research design]].

## Connected notes

[[Edge validation]] · [[Feature engineering]] · [[Overfitting controls]] · [[ML validation]] · [[Research pipelines]]

Focused methods: [[Forecast value and decision mapping]] · [[Market event studies and causal identification]] · [[Execution cost validation protocol]] · [[Edge decay and prospective monitoring]]
