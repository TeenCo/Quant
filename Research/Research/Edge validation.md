# Identifying and Validating a Statistical Edge

An **edge** is a conditional advantage that is observable using information available at a decision time and remains economically useful after uncertainty, risk, and implementation costs. Statistical significance alone is not enough.

## Evidence ladder

1. **Data validity:** point-in-time availability, clean timestamps, correct universe, source lineage, and no accidental future information.
2. **Predictive evidence:** a pre-specified relationship survives dependence-aware uncertainty estimation and correction for the number of attempted ideas.
3. **Robustness:** the result is not driven by a few dates, instruments, parameter values, or a single convenient dataset definition.
4. **Economic plausibility:** a mechanism explains why the pattern may exist and why it may persist, while explicit alternative explanations are considered.
5. **Tradability:** realistic execution and costs leave a useful expected value at the required horizon and capacity.
6. **Persistence:** walk-forward or prospective performance shows manageable regime sensitivity and edge decay.

For inference details, see [[Statistical inference for trading]] and [[Statistical testing pitfalls]]. For economic hypothesis design, see [[Economics-to-market hypotheses]].

## Why a high t-statistic can mislead

The usual single-test threshold assumes that the hypothesis was specified independently of the same data. In a broad search over assets, features, labels, lags, parameter settings, and model classes, the best observed result is selected from many noisy estimates. The effective number of trials can be difficult to reconstruct and trials are correlated. Use a search ledger and methods appropriate to selection and dependence; do not interpret a threshold such as `t > 2` as a universal pass rule.

## Practical checks

- **Target alignment:** returns, labels, and features use correct clocks; no look-ahead, survivorship, or revision leakage.
- **Inference:** uncertainty estimates address heteroskedasticity, serial dependence, overlapping horizons, and small effective sample size.
- **Multiplicity:** log the full search; estimate/adjust for multiple comparisons and selection.
- **Economic magnitude:** report confidence intervals and expected value, not only a p-value. Compare expected value to spread, fees, slippage, impact, financing, borrow, and operational cost.
- **Out-of-sample:** use realistic chronological splits and repeated walk-forward evaluation; avoid repeated peeking at the final holdout.
- **Stress tests:** change plausible assumptions one at a time (cost, delay, rebalance, universe, sample endpoints, data provider) and report sensitivity.
- **Benchmarking:** compare to simple baselines and known exposures; test whether apparent alpha is compensation for risk or a known factor.
- **Capacity:** estimate turnover, market depth, participation, and impact at intended scale.
- **Decay:** model discovery-to-use lag, crowding, structural change, and regime dependence.
- **Reproducibility:** preserve exact data vintages, code, parameters, trial outcomes, and null results.

## Evidence versus interesting leads

An obscure or surprising correlation can be highly valuable for directing research. It remains a **lead** until independently validated, especially if it arose after searching large numbers of unrelated variables. Add it to an experiment ledger with its originating story/source grade, pre-specified test, and explicit invalidation conditions.

## Seed readings

- Harvey, Liu & Zhu, [[Sources/Harvey Liu Zhu 2016|multiple testing in the cross-section of expected returns]].
- Novy-Marx, [[Sources/Novy-Marx 2015|backtesting strategies based on multiple signals]].
- [[Overfitting controls]] · [[Research workflow]] · [[ML validation]] · [[Market microstructure]]
- [[Forecast value and decision mapping]] · [[Execution cost validation protocol]] · [[Edge decay and prospective monitoring]]
