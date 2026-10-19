# Time Series, Dependence, and Forecasting

## Concepts

Time series observations are ordered and often dependent. Key concepts include stationarity, autocorrelation, unit roots, trend/seasonality, cointegration, structural breaks, volatility clustering, state-space models, and forecast-origin evaluation.

## Research workflow

- Clarify sampling frequency, timestamp meaning, and trading calendar.
- Plot and describe levels, returns, volatility, missingness, and regime changes.
- Use transformations appropriate to economic meaning; differencing can remove long-term information.
- Compare simple persistence, mean, seasonal, and linear baselines.
- Use chronological holdouts and rolling forecasts; avoid random split leakage.
- Account for overlap and serial correlation in inference.
- Evaluate forecasts at the decision horizon and measure economic utility net of costs.

## Topics to expand

AR/MA/ARIMA, state-space/Kalman filters, GARCH and realized volatility, cointegration/error correction, point processes, regime switching, spectral methods, high-frequency realized measures, and robust forecast comparison.

For forecast scoring/comparison see [[Forecast evaluation]]; for instability diagnosis see [[Structural breaks and parameter instability]]; for conditional risk estimation see [[Volatility models]].

Focused follow-ups: [[ARIMA and Kalman filtering in real time]] for filtered latent states and sequential forecasts; [[Cointegration estimation and error correction diagnostics]] for residual tests and ECM validation.

## AR(1) worked example and stationarity

Consider \(x_t=c+\phi x_{t-1}+\epsilon_t\), with white-noise innovations of variance \(\sigma_\epsilon^2\). If \(|\phi|<1\), the stationary mean is \(\mu=c/(1-\phi)\), and the centered process has variance \(\sigma_\epsilon^2/(1-\phi^2)\) and autocorrelation \(\rho_k=\phi^k\). The one-step forecast is \(\hat x_{t+1|t}=c+\phi x_t\); the multi-step forecast converges toward the mean as the effect of the current state decays.

If \(\phi\) is near one, shocks decay slowly and finite-sample inference about a unit root becomes delicate. A regression with a trend in nonstationary levels can produce apparently strong relationships between unrelated series. Differencing can remove a stochastic trend but may also discard economically meaningful long-run information. Test and model levels, differences, and cointegrating relations according to the question, not by mechanically applying a stationarity test.

## Cointegration and error correction

Two nonstationary series may have a stationary linear combination, e.g. \(y_t-\beta x_t\). This can represent a long-run equilibrium relation, but estimation uncertainty and structural breaks matter. An error-correction model includes both short-run changes and lagged disequilibrium, such as

\[
\Delta y_t=\alpha(y_{t-1}-\beta x_{t-1})+\sum_i a_i\Delta y_{t-i}+\sum_j b_j\Delta x_{t-j}+u_t.
\]

The sign and magnitude of \(\alpha\) describe adjustment only under the model and identification assumptions. A statistically stationary spread is not automatically mean-reverting net of financing, borrow, execution, and changing hedge ratios. Estimate hedge parameters only with past data and monitor their stability.

## Sampling and calendar effects

Financial series combine regular sessions with closures, overnight risk, auctions, and asynchronous instruments. Define whether a return spans calendar time, trading time, or observation count. Intraday seasonal patterns in volume, volatility, and spread can masquerade as event effects if time-of-day is not controlled. Resampling to bars changes the observation process and may hide jumps or market microstructure noise.

## Connected notes

[[Econometrics]] · [[Probability]] · [[ML validation]] · [[Forex]] · [[Futures]] · [[Crypto]]
