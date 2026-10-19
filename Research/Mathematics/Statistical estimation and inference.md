# Statistical estimation and inference

## Estimators and likelihood

An estimator \(\hat\theta=T(X_1,\ldots,X_n)\) is a random variable; its realized value is an estimate. Bias is \(E[\hat\theta]-\theta\), variance measures sampling dispersion, and mean squared error is variance plus squared bias. Maximum likelihood chooses \(\hat\theta=\arg\max_\theta\sum_i\log f(X_i;\theta)\). Under correct specification, identifiability, regularity, and sufficient data, MLEs are often consistent and asymptotically normal; these are not finite-sample guarantees.

A confidence procedure's 95% coverage means 95% coverage over repeated samples under its assumptions, not a 95% posterior probability for a fixed parameter. A p-value is a tail probability under the null and analysis procedure, not the probability that the null is true.

## Worked example: noisy Sharpe numerator

Let 252 daily iid excess returns have true mean 0.05% and daily standard deviation 1%. The standard error of the sample mean is \(1\%/\sqrt{252}=0.0630\%\). A one-sided 95% lower normal bound is sample mean minus \(1.645(0.0630\%)\); even if the observed mean equals 0.05%, the bound is about −0.0536%. Positive observed performance alone is weak evidence of a positive population mean. Dependence and selection widen the uncertainty further.

## Falsifiable exercise

On a preregistered return series, compare naive iid mean intervals with HAC intervals. Evaluate out-of-sample coverage across rolling periods (where a stable mean is defensible) and record the proportion covering each subsequent-period mean. The proposed inference method fails this diagnostic if observed coverage is materially below its nominal level; this is a diagnostic, not proof of universal coverage.

## Assumptions and failure modes

Likelihood conclusions depend on the sampling model, stationarity, and correct timestamp/universe construction. Non-identifiability, parameter boundaries, heavy tails, dependence, regime shifts, and data snooping can invalidate standard errors and asymptotics. Bootstrap must preserve time dependence and repeat model/feature selection. Economic thresholds should include costs, not merely test against zero.

## Sources

- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) — **Grade 2**, maintained online reference; novelty low; official technical handbook. Reviewed landing page; broad reference, not market-specific and some methods rely on classical designs.
- [ASA statement on statistical significance and p-values](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf) — **Grade 1**, 2016; novelty foundational; professional-society statement. Direct PDF link verified as published URL; clarifies interpretation, not a complete inference textbook.

Related: [[Statistics]] · [[Statistical inference for trading]] · [[Overfitting controls]] · [[Edge validation]]
