# Overfitting, Multiple Testing, and Selection Bias

Overfitting is not limited to complex ML models. It occurs whenever a researcher searches enough variants and reports the lucky winner. Financial data intensifies the problem through autocorrelation, nonstationarity, noisy labels, overlapping outcomes, changing universes, and limited independent observations.

## Common pathways

- Repeatedly tuning on a nominal test set.
- Trying many indicators, assets, horizons, filters, and subgroups, then publishing only the best.
- Selecting only signals with positive in-sample direction before combining them.
- Leakage via revised fundamentals, delayed reporting, corporate actions, index membership, or timestamp mismatch.
- Random folds that mix adjacent or overlapping time windows.
- Backtests with unrealistic fills, costs, liquidity, or execution timing.
- Choosing the sample start/end or benchmark after inspecting results.
- Treating correlated trials as independent for significance calculations, or ignoring their multiplicity entirely.

## Controls

1. Keep a timestamped research/trial ledger, including nulls and abandoned variants.
2. Write hypotheses, target definitions, and validation splits before extensive search.
3. Keep a truly untouched final period or use a prospective forward test; minimize holdout reuse.
4. Use rolling/expanding chronological validation. Purge overlapping labels and consider an embargo around split boundaries.
5. Fit all transforms only on training data; enforce point-in-time features and versioned macro/fundamental vintages.
6. Prefer simple baselines and regularization; evaluate incremental out-of-sample value.
7. Use dependence-aware uncertainty estimates, robust standard errors, bootstrap designs suitable for time series, and multiple-testing-aware statistics.
8. Conduct sensitivity analyses and independent replication on related instruments/data.
9. Include realistic costs and execution constraints before deciding that an edge survives.
10. Monitor decay, drift, and deployment results without retroactively redefining success.

## Important interpretation

No single correction solves all selection bias. The effective trial count is often unknown; procedures rely on assumptions. A clean holdout can be consumed by repeated inspection. Robustness and transparent reporting are essential in addition to formal corrections.

## Worked example: a reused holdout is no longer a holdout

Imagine a researcher uses 2018–2022 for development and labels 2023–2024 “test.” After seeing the first test result, they change the threshold, then the cost model, then the universe, and report only the best final version. The calendar dates are still 2023–2024, but the test outcomes have influenced the design. It is now part of the adaptive search and cannot provide an untouched estimate of the final selected strategy.

Recovering credibility requires a new independent evaluation (for example, a prospective paper-trading period or genuinely unseen dataset), or a transparent nested/walk-forward design that reproduces the complete selection procedure. Do not relabel the same observations as “out of sample” after their results have guided choices.

## Trial accounting protocol

For each attempt, record timestamp, hypothesis version, data snapshot/vintage, universe, target/holding period, features, transformations, model/rule, hyperparameters, validation split, execution assumptions, metrics, plots/reports viewed, and whether results were used to choose the next trial. Include null, negative, failed, and abandoned attempts. A compact trial ledger is more valuable than a sophisticated correction applied to an incomplete search history.

Separate **confirmatory** checks (pre-specified falsification/robustness tests) from **exploratory** searches. Exploratory findings can become new hypotheses, but their apparent significance is not confirmatory evidence; register a fresh test before validating them.

## Corrections and their scope

| Failure mode | Possible control | What it does not solve |
|---|---|---|
| Dependence in returns/losses | HAC errors, block bootstrap, appropriate clustering | Researcher selection, leakage, structural instability |
| Many pre-specified comparisons | Family-wise error or false-discovery procedures | Unknown/adaptive search not represented in the family |
| Adaptive model tuning | Nested chronological validation | Invalid timestamps, bad fills, changing data definitions after outer results are seen |
| Future information in transformations | Fit transforms within each training fold; point-in-time data | Multiple testing or nonstationarity |
| Optimistic execution | Quote-side fills, costs, delay and impact models | Statistical selection or future market changes |

Treat validation design, data integrity, search control, and economic modeling as complementary controls rather than substitutes.

## Readings

- [[Sources/Harvey Liu Zhu 2016]]: factor zoo and multiple-testing hurdle.
- [[Sources/Novy-Marx 2015]]: selecting/composing multiple signals creates severe backtest bias.
- [[Sources/Financial ML field notes]]: financial validation practices and further bibliography.
- [[Edge validation]] · [[Research workflow]] · [[ML validation]]
- [[Statistical testing pitfalls]]: optional stopping, leakage, winner's curse, and dependence.
- [[Selection-aware inference for strategy search]]: null-search derivation and falsifiable simulation.
- [[Sources/Carr Lopez de Prado 2014]]: example of reducing backtest search by deriving rule structure from a process model; its assumptions are specific.
