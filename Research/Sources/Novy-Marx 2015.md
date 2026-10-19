# Backtesting Strategies Based on Multiple Signals

## Bibliography

- **Author:** Robert Novy-Marx
- **Date / version:** NBER Working Paper 21329, July 2015.
- **DOI:** [10.3386/w21329](https://doi.org/10.3386/w21329)
- **Primary source:** [NBER Working Paper 21329](https://www.nber.org/papers/w21329)
- **Full text:** PDF linked from NBER; not copied locally.

## Assessment

- **Evidence grade:** 2 — specialist academic methodological analysis, with transparent theoretical/empirical framing; older and focused on a particular signal-combination setup.
- **Recency:** 2015; foundational warning, but complement with newer methods and current empirical replications.
- **Novelty:** Important demonstration that selecting/composing signals compounds selection bias.
- **Source type:** NBER working paper.

## Summary

The paper analyzes how multi-signal strategies can look highly significant even when their candidate signals have no genuine predictive power. If signals are oriented/selected to have positive in-sample association, choosing combinations introduces large biases. The paper derives and examines t-statistic behavior and emphasizes that signal selection amplifies multiple-testing bias.

## Limitations and research use

- The result addresses a specific signal-selection/composition problem; it is not a universal correction for all strategies.
- Use as a reason to record full research search paths, account for selection, and avoid interpreting a best-of-many backtest as an unbiased estimate.
- Pair with [[Harvey Liu Zhu 2016]] and [[Overfitting controls]].

## Mechanism of the bias

If each noisy signal is oriented or retained because it looked favorable in the same sample, the retained signals have positive estimation error conditional on selection. Combining them does not restore independence from that selection; it can make the resulting strategy appear more precise than the underlying evidence warrants. This is a research-process issue, not a property unique to machine learning.

## Practical translation

Freeze signal definitions and orientation on development data, record all candidate signals (including discarded ones), and evaluate the fixed combination procedure on untouched chronological data. If weights or signs are learned, that learning belongs inside the training/nested validation process. The paper's results motivate selection controls but do not provide a universal correction for every correlated signal family.

## Connected notes

[[Edge validation]] · [[Research workflow]] · [[ML validation]]
