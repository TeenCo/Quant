# Cointegration Estimation and Error-Correction Diagnostics

## Engle–Granger workflow

If \(y_t,x_t\) are each plausibly I(1), estimate \(y_t=\beta_0+\beta_1x_t+u_t\); cointegration requires \(u_t\) to be I(0). An error-correction model is

\[
\Delta y_t=c+\lambda(y_{t-1}-\beta_0-\beta_1x_{t-1})+\sum_i a_i\Delta y_{t-i}+\sum_j b_j\Delta x_{t-j}+e_t.
\]

In the simple scalar case, \(\lambda<0\) indicates correction toward equilibrium. With no other dynamics, approximate half-life is \(\log(0.5)/\log(1+\lambda)\), for \(-1<\lambda<0\).

## Worked example: relative prices

Two related equity-sector log price indexes each trend. Estimate \(\hat\beta=1.2\) on training data and form \(\hat u_t=y_t-\hat\beta_0-1.2x_t\). An ECM estimate \(\hat\lambda=-0.08\) implies a simple half-life near 8.3 periods. This is descriptive: include short-run lags, estimate hedge weights only from prior data, and evaluate stability and net costs out of sample.

## Assumptions and failure modes

- Residual-based unit-root tests have nonstandard critical values; ordinary ADF critical values are inappropriate. Deterministic terms and lag choices matter.
- Searching many pairs and selecting stationary-looking spreads creates selection bias.
- Breaks, changing index composition, dividends, stale prices, and asynchronous observations can mimic mean reversion.
- A stationary spread may adjust too slowly or fail after borrow, financing, and execution costs.
- With multiple endogenous I(1) variables, system/rank methods may be preferable; rank and deterministic terms require justification.

## Falsifiable exercise

Preselect one economically linked pair, fit hedge ratio and ECM on an initial sample, then freeze them for a two-year holdout. Test spread stationarity, negative adjustment, and parameter stability. Falsify stable adjustment if the holdout coefficient is nonnegative, a predeclared stability test rejects, or a fixed reversion rule fails net of costs.

## Claim-specific sources

- Engle–Granger representation and residual cointegration method: grade **2/10**; recency **1987 foundational**; novelty **high historically, established**; source type **peer-reviewed econometrics paper**; [Engle & Granger DOI page](https://doi.org/10.2307/1913236). Bibliographic landing page checked, full text not reviewed. Limit: asymptotic result does not ensure finite-sample power, stable hedge ratios, or tradability.
- Differencing/unit-root practice: grade **2/10**; recency **living online textbook, accessed 2026-10-18**; novelty **low**; source type **open textbook**; [FPP ARIMA chapter](https://otexts.com/fpp3/arima.html). Page directly checked. Limit: not a cointegration-specific critical-value reference.

Related: [[Time series]] · [[Forecast evaluation]] · [[Structural breaks and parameter instability]]
