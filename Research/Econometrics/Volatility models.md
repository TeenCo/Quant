# Volatility Models and Conditional Risk

Volatility is time-varying and clusters: large moves tend to occur near other large moves. Volatility forecasts support sizing, risk limits, option valuation, and cost estimation. They do not automatically forecast return direction or create alpha.

## Model families

- **Historical/realized volatility:** rolling returns or high-frequency realized measures; simple, transparent, window-dependent.
- **EWMA:** exponentially decaying weights; responds smoothly, with decay parameter choice.
- **ARCH/GARCH family:** conditional variance equations; useful baselines, but distribution and persistence assumptions matter.
- **Stochastic volatility:** latent variance process; useful for option and risk models, with estimation complexity.
- **Implied volatility:** option prices transformed under a pricing model; forward-looking risk-neutral quantity, not an unbiased forecast of realized volatility.
- **Range-based and high-frequency estimators:** use intraperiod price paths, subject to microstructure noise, jumps, sampling, and feed quality.

### GARCH(1,1) recursion

A basic conditional variance model is

\[
r_t=\mu+\epsilon_t,\quad \epsilon_t=\sqrt{h_t}z_t,\quad h_t=\omega+\alpha\epsilon_{t-1}^2+\beta h_{t-1},
\]

with \(\omega>0\), \(\alpha,\beta\ge0\), and often \(\alpha+\beta<1\) for finite long-run variance under standard assumptions. The previous squared shock updates risk; persistence \(\alpha+\beta\) controls decay. This model is a benchmark, not a universal law: leverage effects, jumps, fat tails, changing regimes, and mean misspecification can matter. Fit distributional assumptions on training data and assess forecast calibration and tail coverage out of time.

### Realized variance and sampling

For intraday log returns \(r_{t,j}\), realized variance is \(RV_t=\sum_j r_{t,j}^2\). Under ideal continuous-price/noise-free assumptions, finer sampling can improve measurement of integrated variance; observed prices contain bid-ask bounce, discreteness, asynchronous updates, and jumps. Extremely fine sampling can therefore add noise. Specify sampling frequency, overnight return treatment, jump handling, and data cleaning; compare multiple reasonable estimators as sensitivity analysis.

## Forecast design

Specify return interval, horizon, annualization, overnight/intraday split, market calendar, and whether jumps are included. Use only past observations at each origin. Compare forecast variance to realized variance using losses appropriate to positive variance targets, such as QLIKE or log variance loss, plus calibration and tail diagnostics.

## Applications and cautions

- **Risk sizing:** target volatility changes leverage and exposures; include leverage bounds, turnover, and stressed liquidity.
- **Execution costs:** spread/impact often depend on volatility, so costs should be state-dependent.
- **Options:** implied volatility includes risk premia and measurement/model conventions; option-implied variance need not equal expected physical variance.
- **Regime variation:** volatility forecasts can fail at structural breaks and after market closures or data outages.

## Forecast example and scaling

If daily variance forecasts are \(\hat h_{t+1},\ldots,\hat h_{t+H}\), a simple forecast of cumulative variance is their sum only under the return/variance definition and model assumptions used; cumulative volatility is the square root of that sum, not the sum of volatilities. Annualization convention (trading days vs calendar time, overnight inclusion) must match the realized target. A volatility-targeting position may use \(w_t\propto\sigma^*/\hat\sigma_t\), but add leverage caps, forecast lag, rebalance schedule, turnover, and state-dependent costs; scaling changes exposures and risk, not necessarily expected return.

For volatility-managed portfolio literature, see [[Sources/Moreira Muir 2017]]. Their study is a portfolio-risk scaling result and should be independently replicated under point-in-time forecasts and realistic costs. For option-implied versus physical variance and VIX, see [[Markets/Options/Implied volatility, variance risk premium and VIX]].

For likelihood estimation, standardized-residual checks, ARCH diagnostics, and a falsifiable rolling comparison, see [[GARCH estimation and residual diagnostics]].

Related: [[Probability]] · [[Time series]] · [[Forecast evaluation]] · [[Options]] · [[Execution costs and market impact]] · [[Edge validation]]
