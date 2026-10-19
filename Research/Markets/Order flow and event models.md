# Order Flow and Event Models

Order flow summarizes marketable demand and supply and the sequence of market events. It may reveal liquidity consumption or short-lived imbalance, but observed flow can be endogenous, venue-specific, and quickly arbitraged.

## Event-time perspective

Instead of fixed clock bars, event-time methods analyze trade, quote, cancellation, or book-update arrivals. This can better reflect market activity during fast and slow periods, but event sampling changes the statistical question and can induce sampling bias.

## Hawkes processes

A Hawkes process models event intensity as a baseline plus excitation from prior events. In multivariate models, one event type or instrument can raise the conditional rate of another. These models are useful for describing clustering and event dependence; fitted excitation is not itself proof of a causal mechanism or tradable alpha.

### Practical fit/evaluation checklist

- First remove or model intraday/weekly seasonality and exogenous common-news effects.
- Define event categories consistently and specify feed/venue filters.
- Check stationarity/stability and kernel identifiability; examine residual time-rescaling diagnostics.
- Compare to inhomogeneous Poisson, self-exciting alternatives, and simple intensity baselines.
- Fit only on training windows; check parameter stability and event prediction/calibration out of sample.
- Evaluate whether added forecast information changes a feasible execution decision after latency, spread, fees, and impact.

## Other order-flow measures

Order-flow imbalance, signed volume, queue imbalance, trade intensity, and cancellation/addition rates are definitions, not universal observables. Record the signing rule, venue consolidation, timestamp convention, depth level, and handling of ambiguous/missing messages. Avoid interpreting buy-sell imbalance as informed demand without alternative explanations.

## Research lead

[[Sources/Bacry Mastromatteo Muzy 2015]] reviews Hawkes process applications in finance, including transaction volatility, systemic contagion, execution, and order-book dynamics. See [[Sources/Hawkes processes lead]] for candidate tests.

## Connected notes

[[Market microstructure]] · [[Order book data and event-time reconstruction]] · [[Execution costs and market impact]] · [[Probability]] · [[Time series]] · [[Forex]] · [[Crypto]] · [[Futures]]
