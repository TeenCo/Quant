# Econometrics and Empirical Methods

Econometrics combines economic models, probability, and statistics to estimate relationships and assess uncertainty in observed data. For market research, it is crucial to distinguish association, prediction, and causation.

## Core toolkit

- Regression and regularization; identification assumptions and omitted-variable bias.
- Time-series estimation, stationarity, cointegration, volatility models, and forecast evaluation.
- Panel data, cross-sectional inference, clustered and heteroskedasticity-robust errors.
- Causal designs: experiments, difference-in-differences, instrumental variables, regression discontinuity, synthetic controls, event studies.
- Robustness, placebo, sensitivity, external validity, and measurement error.

## Financial adaptations

Returns may be serially dependent, heavy-tailed, heteroskedastic, and overlapping. The universe and data vintage change over time; market participants anticipate public information. A sound method depends on the estimand and data-generating process, not on a single “best” estimator.

## Regression decomposition and interpretation

In a linear projection \(y=X\beta+u\), least squares estimates a best linear approximation under a chosen sample and loss. A coefficient is not automatically causal: causal interpretation requires an identification design and assumptions that address omitted variables, assignment, measurement, and selection. For prediction, coefficients can still be useful without being structural, but performance must be assessed on future data with an appropriate benchmark.

With heteroskedasticity, the conventional homoskedastic covariance estimator is generally inconsistent. With serial dependence, HAC covariance estimators can adjust uncertainty under assumptions; with grouped shocks, clustered inference may be more appropriate. Choose the estimator based on the dependence-generating process and observation unit. Robust standard errors affect estimated uncertainty, not the point estimate or data validity.

## Example: panel event-study specification

A common descriptive panel form is \(y_{it}=\alpha_i+\lambda_t+\beta D_{it}+\epsilon_{it}\), with unit and time effects. The coefficient \(\beta\) has a causal interpretation only under the design's assumptions; fixed effects do not remove time-varying confounding, anticipation, spillovers, or measurement problems. Standard errors should reflect treatment assignment and shared shocks (for example, clustering by assignment unit where justified), and the estimand should match the weights implicit in the estimator.

## Model selection and specification

Functional forms, lags, controls, transformations, sample windows, and subgroups are all researcher choices. Pre-specify primary analyses where possible, record exploratory variants, and separate model diagnostics from confirmatory claims. A large sample can yield tiny p-values for negligible effects; report magnitude and interval. A flexible model may improve prediction while obscuring structural interpretation. State which objective the analysis serves.

## Applications and reading leads

- [[Statistical inference for trading]] and [[Statistical testing pitfalls]] organize dependence, selection, and interpretation issues for trading research.
- [[Sources/Moreira Muir 2017]] is a portfolio-level example of conditional risk scaling; it is not a universal volatility-timing rule.
- [[Sources/Davis Fuenzalida Taylor 2019]] is a macro-finance example combining latent trend estimates and bond-risk-premium models.
- [[Sources/Carr Lopez de Prado 2014]] explores reducing backtest search through a model-derived rule under a specific stochastic-process setup.
- [[Sources/Bacry Mastromatteo Muzy 2015]] maps point-process applications to market microstructure.

## Reading

See [[Sources/Athey Imbens 2017]] for a review of identification and causal inference and [[Time series]] for dependence-specific concerns.
