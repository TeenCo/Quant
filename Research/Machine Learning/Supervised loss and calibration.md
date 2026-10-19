# Supervised Loss and Probability Calibration

## Core idea

The loss defines which errors the fitted model prioritizes; it does not itself guarantee that predicted probabilities match event frequencies. For binary outcomes, log loss is
\[
L=-\frac1N\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)],
\]
and the Brier score is \(N^{-1}\sum_i(p_i-y_i)^2\). Both are proper scoring rules: in expectation, truthful probabilities minimize score. A calibrated forecast satisfies approximately \(P(Y=1\mid \hat p=p)=p\). Reliability diagrams and calibration intercept/slope diagnose this relation; discrimination (AUC/rank) is a different property. A decision threshold follows payoffs and costs, not a default 0.5.

In markets, calibrate probabilities of a positive net return or fill event on chronologically held-out predictions; evaluate scores and realized utility separately. A high AUC can coexist with badly calibrated tail probabilities or negative net value.

## Leakage and validation failures

- Fit Platt/logistic or isotonic calibration only on out-of-fold/validation predictions, never in-sample fitted values or the final test.
- Preserve chronology and purge overlapping outcome intervals; calibrator training labels must have matured before the forecast origin.
- Class reweighting, undersampling, and case-control sampling change the apparent base rate; correct/validate probabilities against the deployment prevalence.
- Isotonic calibration can overfit small effective samples; assess by period and report uncertainty. Repeatedly selecting calibration methods on the outer test consumes that test.
- Overlapping labels reduce effective sample size; confidence bands based on independent rows are optimistic.

## Research exercise

For a daily event-direction model, generate nested walk-forward predictions. Compare raw probabilities, logistic calibration, and isotonic calibration using Brier/log scores, calibration slope/intercept, and net utility at a threshold fixed from inner validation after costs. Report each outer fold and test whether calibration survives high- and low-volatility eras.

## Sources (graded)

- **Grade 1** — Gneiting & Raftery (2007), *Strictly Proper Scoring Rules, Prediction, and Estimation*, JASA. Recency: foundational (2007); novelty: general theory. Type: peer-reviewed methods review. Direct: https://doi.org/10.1198/016214506000001437 . Limit: not finance-specific; calibration and proper scoring are related but distinct.
- **Grade 2** — Niculescu-Mizil & Caruana (2005), *Predicting Good Probabilities with Supervised Learning*, ICML. Recency: older (2005); novelty: empirical comparison. Type: conference paper. Direct: https://www.cs.cornell.edu/~alexn/papers/calibration.icml05.crc.rev3.pdf . Limit: benchmarks are not nonstationary financial time series.
