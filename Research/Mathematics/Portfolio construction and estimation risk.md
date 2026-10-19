# Portfolio Construction and Estimation Risk

Portfolio construction maps forecasts and risk estimates into weights. The optimizer is only as credible as its inputs, constraints, cost model, and point-in-time universe.

## Mean-variance setup

For expected excess returns \(\mu\), covariance \(\Sigma\), weights \(w\), and risk-aversion \(\lambda>0\), a basic objective is

\[
\max_w\; \mu^Tw-\frac{\lambda}{2}w^T\Sigma w
\quad\text{subject to }\mathbf{1}^Tw=1.
\]

Without further constraints and for positive-definite \(\Sigma\), the solution is

\[
w=\frac{1}{\lambda}\Sigma^{-1}(\mu-\nu\mathbf{1}),\qquad
\nu=\frac{\mathbf{1}^T\Sigma^{-1}\mu-\lambda}{\mathbf{1}^T\Sigma^{-1}\mathbf{1}}.
\]

The inverse covariance amplifies estimation noise in low-variance directions. If the estimated returns are small relative to their uncertainty, optimizer weights can become extreme and unstable. Constraints (long-only, leverage, sector, turnover, liquidity) change the solution and must be recorded as part of the strategy.

## Worked intuition: two assets

For two assets with equal expected returns and equal variance, positive correlation reduces diversification benefit; the unconstrained minimum-variance portfolio is symmetric. If the estimated correlation falls slightly below zero, the optimizer may assign concentrated or offsetting positions. With finite data, that small sign change may be estimation noise. Compare weights under a range of covariance estimates and use shrinkage or robust constraints; judge stability and realized net outcomes, not just in-sample variance.

## Turnover-aware objective

A practical objective can penalize trading from current weights \(w_0\):

\[
\max_w\; \mu^Tw-\frac{\lambda}{2}w^T\Sigma w-C(w-w_0),
\]

where \(C\) may include linear spread/fees and nonlinear impact/borrow estimates. Cost estimates are uncertain and endogenous to liquidity. Rebalance timing, partial fills, and binding constraints can make actual exposure differ from target weights; evaluate realized holdings and costs.

## Robustness protocol

1. Estimate \(\mu\) and \(\Sigma\) using only the training window; document horizons and units.
2. Compare equal-weight, minimum-variance, benchmark, and forecast-driven allocations.
3. Perturb expected returns/covariances within plausible estimation uncertainty and record weight sensitivity.
4. Enforce gross/net leverage, concentration, sector, liquidity, borrow, and turnover constraints.
5. Include fees, spreads, financing, market impact, and a capacity curve.
6. Evaluate weights on chronological out-of-sample data; report realized risk, returns, drawdown/tails, turnover, exposures, and constraint breaches.

## Sources and evidence

- **Harry Markowitz (1952), “Portfolio Selection,” *The Journal of Finance*.** Grade 2 for the foundational mean-variance framework; recency: foundational; novelty: foundational; source type: peer-reviewed theory paper. [DOI](https://doi.org/10.1111/j.1540-6261.1952.tb01525.x). Limitation: the model assumes inputs and constraints that are difficult to estimate/implement; it does not establish realized strategy performance.
- **Olivier Ledoit & Michael Wolf (2004), “Honey, I Shrunk the Sample Covariance Matrix,” *The Journal of Portfolio Management*.** Grade 2 for covariance shrinkage methodology; recency: foundational; novelty: established estimation technique; source type: peer-reviewed methods paper. [Author-hosted paper](https://www.ledoit.net/honey.pdf). Limitation: shrinkage improves estimation under its setup, but does not guarantee optimal portfolio utility in every market or with arbitrary costs.

## Exercise

Using a small point-in-time asset universe, compare equal-weight, sample-covariance minimum variance, and one pre-specified shrinkage portfolio. Use expanding chronological estimation; report turnover, max weight, realized volatility, and net performance. Add a small perturbation to each mean/covariance input and quantify weight sensitivity. State whether any result is a forecasting claim, a risk-allocation result, or neither.

Related: [[Convexity and constrained optimization]] · [[Regression covariance and PCA]] · [[Edge validation]] · [[Execution cost validation protocol]] · [[Overfitting controls]]
