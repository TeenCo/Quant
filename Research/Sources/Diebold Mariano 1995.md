# Comparing Predictive Accuracy

## Bibliography

- **Authors:** Francis X. Diebold and Roberto S. Mariano
- **Date / version:** NBER Technical Working Paper 0169, November 1994; published in *Journal of Business & Economic Statistics* 13 (1995), pp. 253–265.
- **DOI:** [10.3386/t0169](https://doi.org/10.3386/t0169)
- **Source:** [NBER Working Paper T0169](https://www.nber.org/papers/t0169)

## Assessment

- **Evidence grade:** 2 — foundational scholarly forecasting methodology paper; its application requires correct loss, dependence, and model-selection treatment.
- **Recency:** 1995; still a central reference, but pair with later refinements and current forecast-design literature.
- **Novelty:** Foundational method; low novelty, high methodological relevance.
- **Source type:** Published academic paper / NBER technical working paper.

## Summary and use

The Diebold–Mariano approach compares forecast accuracy by examining a time series of loss differentials between two forecasts and testing whether the expected differential is zero. Serial dependence in the loss differential is important, particularly with multi-step or overlapping forecast horizons.

## Caveats

- The test does not correct for broad model search or repeated holdout use.
- Test conclusions depend on forecast origins, loss function, horizon, and long-run variance estimation.
- Equal predictive accuracy is distinct from equal trading utility; implementability and transaction costs require separate evaluation.

## Loss-differential interpretation

Given forecasts A and B, define \(d_t=L(e_{A,t})-L(e_{B,t})\) under one predeclared loss. A negative mean favors A in the evaluation sample. The test standardizes that mean by an estimate of the long-run variance of \(d_t\), so serial dependence matters. The test asks about expected predictive loss under the specified design; it neither selects a loss for the researcher nor resolves broad model search, nonstationarity, or whether the forecast changes net decisions.

Related: [[Forecast evaluation]] · [[Time series]] · [[Overfitting controls]] · [[Edge validation]]
