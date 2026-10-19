# Volatility-Managed Portfolios

## Bibliography

- **Authors:** Alan Moreira and Tyler Muir
- **Date / version:** NBER Working Paper 22208, April 2016 (revised June 2016); published in *The Journal of Finance* 72(4), 2017, 1611–1644.
- **DOI:** [10.1111/jofi.12513](https://doi.org/10.1111/jofi.12513)
- **Primary source:** [NBER Working Paper 22208](https://www.nber.org/papers/w22208)

## Assessment

- **Evidence grade:** 2 — peer-reviewed finance paper and influential portfolio result; sample, factors, implementation, and later replication/critique matter for generalization.
- **Recency:** 2017; well-established, but market regimes and practical cost assumptions evolve.
- **Novelty:** Demonstrates dynamic risk scaling as a portfolio-construction dimension across multiple factors and currency carry.
- **Source type:** Peer-reviewed journal article / NBER working paper.

## Summary

The paper studies scaling exposure down when realized volatility is high. The authors report improved Sharpe ratios and utility for several equity factors and currency carry, arguing that factor expected returns do not rise proportionally with volatility. This is a dynamic allocation/risk-scaling result, not necessarily evidence of a standalone forecasting signal or free alpha.

## Research use and limitations

- Distinguish a change in risk from an increase in expected return; risk scaling can improve a metric while changing leverage, turnover, and crash exposure.
- Test volatility estimators, lags, lookback choices, transaction costs, leverage constraints, and volatility spikes.
- Use strictly lagged, point-in-time estimates and compare against fixed-risk, volatility-targeted, and other simple baselines.
- Study subsequent critiques, replications, and live implementability before relying on the reported improvement.

## Replication design

Separate the question “does scaling alter risk-adjusted portfolio outcomes?” from “does a volatility forecast predict returns?” Recreate the original portfolio and scaling rule as closely as permitted, then test a frozen implementation with lagged forecasts, leverage bounds, turnover, costs, and chronological evaluation. Compare fixed exposure, volatility-targeted exposure, and a simple risk control under identical dates. Report return, volatility, drawdown/tails, exposures, and turnover so improved Sharpe is not mistaken for higher alpha.

## Connected notes

[[Edge validation]] · [[Statistical inference for trading]] · [[Probability]] · [[ETFs]] · [[Forex]] · [[Overfitting controls]]
