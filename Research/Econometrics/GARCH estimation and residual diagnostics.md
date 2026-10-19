# GARCH Estimation and Residual Diagnostics

## Estimation target

For \(r_t=\mu_t+\epsilon_t\), \(\epsilon_t=\sqrt{h_t}z_t\),

\[
h_t=\omega+\alpha\epsilon_{t-1}^2+\beta h_{t-1},\quad \omega>0,\;\alpha,\beta\ge0.
\]

Under standard conditions \(\alpha+\beta<1\) gives unconditional variance \(\omega/(1-\alpha-\beta)\). Fit by likelihood with an explicitly stated innovation distribution and compare on identical samples/origins.

## Worked diagnostic pass

Fit a constant-mean GARCH(1,1) to daily log returns. Compute standardized residuals \(\hat z_t=\hat\epsilon_t/\sqrt{\hat h_t}\). Check their ACF/Ljung–Box for residual mean dependence; check squared standardized residual ACF and ARCH-LM for remaining variance dependence; inspect tail quantiles, exceedance clustering, optimizer convergence, boundary estimates, and persistence. Compare Gaussian and Student-t innovations, then assess one-step variance forecasts against realized variance using QLIKE and calibration out of sample.

## Assumptions and failure modes

- Symmetric GARCH gives equal variance response to positive/negative shocks; leverage may require another specification.
- Persistence near one is uncertain and may proxy for regime change.
- Fat tails, jumps, intraday seasonality, stale prices, and mean misspecification distort likelihood and diagnostics.
- Boundary parameters and optimizer convergence deserve explicit reporting.
- Realized variance depends on sampling, overnight treatment, and microstructure noise.

## Falsifiable exercise

For one liquid futures contract, compare rolling one-step Gaussian GARCH, Student-t GARCH, and EWMA forecasts. Reject “GARCH adds value” if it fails to reduce predeclared QLIKE versus EWMA with dependence-aware uncertainty, or if standardized residual squares retain predeclared significant dependence.

## Claim-specific sources

- ARCH conditional heteroskedasticity and estimation: grade **2/10**; recency **1982 foundational**; novelty **high historically, low now**; source type **peer-reviewed Econometrica paper**; [Engle DOI record](https://doi.org/10.2307/1912773). Bibliographic landing page checked, not full text. Limit: foundational ARCH result, not a survey of modern GARCH or evidence of market utility.
- Realized-variance framework: grade **2/10**; recency **2001 foundational**; novelty **high historically**; source type **peer-reviewed Journal of Econometrics article**; [Andersen et al. DOI page](https://doi.org/10.1016/S0304-4076(00)00071-3). Bibliographic landing page only checked. Limit: asymptotic measurement claims depend on sampling and price-process assumptions.

Related: [[Volatility models]] · [[Forecast evaluation]] · [[Time series]] · [[Execution costs and market impact]]
