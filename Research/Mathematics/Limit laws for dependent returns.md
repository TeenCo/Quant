# Limit laws for dependent returns

## LLN, CLT, and what they do not say

For iid integrable observations, the law of large numbers gives \(\bar X_n\to E[X]\) (almost surely under standard conditions). With finite variance \(\sigma^2\), the iid central limit theorem gives \(\sqrt n(\bar X_n-\mu)/\sigma\Rightarrow N(0,1)\). The CLT is an approximation to a sampling distribution, not a claim that individual returns are Gaussian.

For a weakly dependent stationary sequence with summable autocovariances and suitable moment/mixing conditions, the asymptotic variance is the long-run variance \(\Omega=\gamma_0+2\sum_{k\ge1}\gamma_k\), not simply \(\gamma_0\). These conditions can fail with unit roots, long memory, infinite variance, structural breaks, or volatility dynamics that invalidate a chosen approximation.

## Worked finance example

For AR(1) daily returns with lag correlation \(\rho=0.2\), the long-run variance factor relative to the one-day variance is \((1+\rho)/(1-\rho)=1.5\). At \(n=1000\), iid standard error is \(\sigma/\sqrt{1000}\); long-run standard error is about \(\sqrt{1.5}=1.225\) times larger. A nominal t-statistic of 2 would become approximately 1.63 under this simplified dependence model.

## Falsifiable exercise

Simulate 10,000 AR(1) return samples of length 500 at \(\rho=0.2\), and estimate mean-interval coverage using iid SE versus a Newey–West/HAC SE. Test whether nominal 95% coverage is closer to 95% with HAC. Repeat under a variance break and document that standard stationary HAC may still mis-cover.

## Assumptions and failure modes

The iid CLT needs finite variance; dependence CLTs need additional stationarity, weak-dependence, and moment assumptions. Heavy tails can make Gaussian approximations slow or invalid. Overlapping horizons mechanically induce dependence. HAC bandwidth selection matters, and no asymptotic standard error repairs look-ahead or multiple-selection bias.

## Sources

- [Newey & West (1987), A Simple, Positive Semi-definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix](https://www.jstor.org/stable/1913610) — **Grade 1**, 1987; novelty foundational; peer-reviewed econometrics article. Bibliographic page reviewed; paywall may restrict full text. Establishes a HAC estimator, not universal validity under breaks or arbitrary dependence.
- [Statlect: conditional expectation](https://www.statlect.com/fundamentals-of-probability/conditional-expectation) — **Grade 3**, 2021; low novelty; online lecture. Reviewed for supporting expectation concepts; not the source for CLT conditions.

Related: [[Probability]] · [[Statistics]] · [[Time series]] · [[Forecast evaluation]]
