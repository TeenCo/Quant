# Statistical Inference and Estimation

Statistical methods quantify what finite, noisy observations say about an underlying process. In quantitative finance, observations are typically dependent, heteroskedastic, selected, and subject to structural change.

## Topics

- Estimation: bias, variance, consistency, likelihood, Bayesian inference.
- Uncertainty: standard errors, confidence/credible intervals, bootstrap and permutation methods.
- Testing: null hypotheses, effect size, power, false discovery, multiple comparisons.
- Regression: omitted variables, regularization, robust errors, diagnostics.
- Time dependence: autocorrelation, heteroskedasticity, overlapping outcomes, regime shifts.
- Selection: data snooping, publication bias, survivorship, winner's curse.

## Practical principle

Report estimates with uncertainty, the effective search space, data construction, and assumptions. A small p-value does not fix invalid measurement, leaked information, large-scale selection, or impractical costs. See [[Edge validation]] and [[Overfitting controls]].

## Worked derivation: uncertainty in a sample mean under dependence

Suppose a strategy produces a stationary return series \(r_t\) with mean \(\mu\), variance \(\gamma_0\), and autocovariance \(\gamma_k=\operatorname{Cov}(r_t,r_{t-k})\). The sample mean is \(\bar r=n^{-1}\sum_{t=1}^{n}r_t\). Its variance is

\[
\operatorname{Var}(\bar r)=\frac{1}{n^2}\left[n\gamma_0+2\sum_{k=1}^{n-1}(n-k)\gamma_k\right]
\approx \frac{1}{n}\left(\gamma_0+2\sum_{k=1}^{\infty}\gamma_k\right),
\]

when the autocovariances are summable and the sample is sufficiently long. Under independence, all \(\gamma_k=0\) for \(k>0\), giving the familiar \(\gamma_0/n\). Positive dependence increases uncertainty in the average; negative dependence can reduce it. Thus the nominal row count alone does not determine precision.

For intuition, if daily returns were an AR(1) process with lag-one correlation \(\rho\), a rough long-run effective sample size is

\[
n_{\text{eff}}\approx n\frac{1-\rho}{1+\rho}.
\]

At \(n=1{,}000\) and \(\rho=0.2\), this approximation gives about 667 independent-observation equivalents, not 1,000. This is an illustration, not a universal estimator: higher-order dependence, heteroskedasticity, overlapping labels, and cross-sectional common shocks require more careful covariance estimation.

### HAC standard error in practice

For estimated mean \(\bar r\), a heteroskedasticity-and-autocorrelation-consistent estimator estimates the long-run variance using weighted sample autocovariances:

\[
\widehat{\Omega}=\hat\gamma_0+2\sum_{k=1}^{L}w_k\hat\gamma_k,
\qquad \widehat{SE}(\bar r)=\sqrt{\widehat{\Omega}/n}.
\]

The truncation lag \(L\) and weights \(w_k\) matter. They should reflect the sampling and overlap design rather than be tuned to produce significance. For panel strategies, dependence can also be shared across assets or dates; cluster choices must follow the economic sampling design.

## Why Sharpe annualization can fail

For a one-period excess-return series with mean \(\mu\) and standard deviation \(\sigma\), the one-period Sharpe ratio is \(S=\mu/\sigma\). The familiar \(\sqrt{q}\) annualization, \(S_q=\sqrt{q}S\), assumes independent, identically distributed increments with variance scaling linearly in time and a consistent return definition. With autocorrelation \(\rho_k\), the variance of a \(q\)-period sum is

\[
\operatorname{Var}\left(\sum_{t=1}^{q}r_t\right)=q\gamma_0+2\sum_{k=1}^{q-1}(q-k)\gamma_k,
\]

so annualized risk and Sharpe need not follow square-root-of-time scaling. Overlapping return construction can induce exactly this kind of dependence. Report the sampling interval, aggregation convention, and dependence-aware uncertainty alongside annualized performance.

## Intervals and tests: conditions before formulas

A confidence interval is a procedure with a coverage claim under assumptions; it is not a probability statement about a fixed parameter after observing the data. A conventional standard error can be misleading if the model was selected on the same sample, the target was revised after observation, or the sampling distribution is dominated by rare tail events. Bootstrap resampling must preserve relevant dependence (for example, moving/stationary blocks for time series) and must repeat the entire selection process when quantifying winner's-curse uncertainty.

Use a null and alternative that match the decision. A test of \(\mu=0\) is not necessarily the test of interest if the required hurdle is costs plus capital charges. Prefer an interval for net expected return or a minimum economically meaningful effect, and distinguish “evidence against zero” from “evidence of sufficient value.” See [[Statistical inference for trading]], [[Forecast evaluation]], and [[Statistical testing pitfalls]].

## Research checklist

1. State the estimand, units, horizon, observation unit, and target population/universe.
2. Draw the dependence structure: time overlap, asset clustering, event clustering, and common factors.
3. Choose an uncertainty method that respects that structure; state bandwidth, cluster, or block choices.
4. Report point estimate, uncertainty interval, effect size, and economically relevant hurdle.
5. Account for the full search and selection procedure; preserve null trials.
6. Stress tails and regimes; do not let one asymptotic p-value substitute for robustness.

Connected: [[Probability]] · [[Time series]] · [[Forecast evaluation]] · [[Statistical inference for trading]] · [[Overfitting controls]] · [[Edge validation]]

Focused foundation: [[Statistical estimation and inference]]
