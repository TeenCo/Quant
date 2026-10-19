# Hawkes Processes: High-Frequency Research Lead

## Source

- Bacry, Mastromatteo & Muzy, [[Bacry Mastromatteo Muzy 2015|“Hawkes processes in finance”]], arXiv review (2015).
- **Evidence grade:** 2 for the review as a scholarly literature map; application-specific alpha claims require separate tests.
- **Recency:** Review published 2015; foundational overview, not a current market-data assessment.
- **Novelty:** Moderate as a research application family; model class is established.
- **Source type:** Academic review/preprint.

## Candidate questions

- Do trade arrivals or order-book events display stable self- or cross-excitation after accounting for common news and diurnal intensity?
- Does event clustering differ by venue, liquidity, volatility, or market session?
- Can a point-process model improve short-horizon intensity forecasts relative to non-Hawkes baselines, and does the improvement persist after latency/costs?
- Do cross-asset excitation estimates add information beyond shared market/sector factors?

## Necessary controls

Check timestamp ordering/resolution, batching and feed filters, daylight/session seasonality, endogenous versus exogenous drivers, parameter stability, kernel misspecification, branching stability, and out-of-time likelihood/calibration. Do not interpret fitted excitation as causality without identification.

Related: [[Market microstructure]], [[Probability]], [[Crypto]], [[Forex]], [[Futures]], [[Edge validation]].
