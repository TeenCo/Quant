# Hawkes Processes in Finance

## Bibliography

- **Authors:** Emmanuel Bacry, Iacopo Mastromatteo, Jean-François Muzy
- **Date / version:** arXiv review submitted February 2015, revised May 2015.
- **Source:** [arXiv:1502.04592](https://arxiv.org/abs/1502.04592)
- **Full text:** [arXiv PDF](https://arxiv.org/pdf/1502.04592); see arXiv license terms before local copying.

## Assessment

- **Evidence grade:** 2 — scholarly review of a mature mathematical/statistical literature with broad finance applications; review is older and findings need current application-specific validation.
- **Recency:** 2015; foundational survey, not a current empirical audit of any particular market.
- **Novelty:** Useful synthesis of self-/cross-exciting point-process models in high-frequency finance.
- **Source type:** Academic review/preprint.

## Summary

Hawkes processes model event arrivals whose conditional intensity depends on past events. The review describes applications to transaction-level volatility, market stability, systemic contagion, optimal execution, and order-book dynamics. Multivariate formulations can represent cross-excitation among event types or instruments.

## Research use and caveats

Event clustering can reflect endogenous excitation, common exogenous news, or measurement/venue effects; a fitted self-excitation parameter is not automatically causal. Check stationarity/stability, timestamp quality, omitted common shocks, kernel choice, sampling, and out-of-sample calibration. Tick-level model fit does not establish exploitable net alpha.

## Minimal model interpretation

A univariate Hawkes process has conditional intensity \(\lambda(t)=\mu+\sum_{t_i<t}g(t-t_i)\), where \(\mu\) is baseline intensity and \(g\) captures excitation after earlier events. A multivariate model adds cross-event kernels. The kernels describe conditional arrival clustering under the specified model; they do not identify whether the cause is strategic reaction, common news, or omitted state variables. Compare against a time-of-day baseline and include exogenous covariates before interpreting excitation.

## Connected notes

[[Probability]] · [[Market microstructure]] · [[Time series]] · [[Forex]] · [[Crypto]] · [[Futures]] · [[Edge validation]]
