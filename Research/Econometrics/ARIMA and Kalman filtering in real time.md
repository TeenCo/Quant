# ARIMA and Kalman Filtering in Real Time

## Model

ARIMA models forecast observed dependence: \(\phi(B)(1-B)^d y_t=c+\theta(B)\epsilon_t\). State-space models separate observation noise from latent dynamics:

\[
y_t=Z_t\alpha_t+\varepsilon_t,\qquad \alpha_{t+1}=T_t\alpha_t+R_t\eta_t.
\]

Given prior state mean \(a_t\) and covariance \(P_t\), the Kalman innovation is \(v_t=y_t-Z_ta_t\), its variance \(F_t=Z_tP_tZ_t'+H_t\), and gain \(K_t=P_tZ_t'F_t^{-1}\). The filtered state is \(a_t+K_tv_t\). Filtering uses information through \(t\); smoothing uses later observations and is retrospective.

## Worked example: latent price trend

Let \(\alpha_t=(\mu_t,\nu_t)'\) be local level and slope, \(Z=(1,0)\), and \(T=\begin{pmatrix}1&1\\0&1\end{pmatrix}\). Treat a noisy daily macro surprise index as observation of \(\mu_t\). Estimate level, slope, and measurement variances on training data, then update only when each release becomes available. High measurement noise relative to state noise produces a small gain and smoother trend. Compare the filtered forecast against random-walk and expanding-mean forecasts at identical release-time origins.

## Assumptions and failure modes

- Linear Gaussian likelihood is exact for Gaussian disturbances; non-Gaussian tails invalidate Gaussian interval interpretations.
- ARIMA differencing can remove meaningful long-run information or mistake a break for a unit root; order selection can be fragile in short samples.
- State variance near zero can make parameters weakly identified and likelihood optimization sensitive to initialization.
- Smoothed states leak future information if used as historical trading features; use filtered states.
- Missing observations can omit measurement updates, but state-dependent missingness needs a model.

## Falsifiable exercise

Using a public macro release series, compare expanding mean, ARIMA(0,1,1), and local-level Kalman one-step forecasts on a fixed chronological holdout. Pre-register squared-error loss and 90% interval coverage. Reject improvement if Kalman loss is not lower with dependence-aware uncertainty or intervals materially undercover.

## Claim-specific sources

- ARIMA construction, differencing, MLE/order selection, diagnostics: grade **2/10**; recency **living online textbook, accessed 2026-10-18**; novelty **low**; source type **open textbook**; [FPP ARIMA chapter](https://otexts.com/fpp3/arima.html). Page directly checked. Limit: not evidence of financial forecast performance.
- Local trend state-space form and Kalman/MLE implementation: grade **2/10**; recency **statsmodels 0.15.0 docs, accessed 2026-10-18**; novelty **moderate for implementation**; source type **official software documentation**; [statsmodels example](https://www.statsmodels.org/stable/examples/notebooks/generated/statespace_local_linear_trend.html). Page directly checked. Limit: implementation example, not an independently validated market signal.

Related: [[Time series]] · [[Forecast evaluation]] · [[Structural breaks and parameter instability]]
