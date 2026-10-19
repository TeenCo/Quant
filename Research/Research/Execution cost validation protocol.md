# Execution-Cost Validation Protocol

## Decomposition and example

For a buy with decision mid 100 and fill 100.03 plus 0.01 fees, realized shortfall is 4 cents/unit before any unfilled opportunity cost. A mid-price backtest reporting +3 cents is negative under that fill. Keep benchmark, side, and clocks fixed; model spread, fees, delay, impact, partial fills, and unfilled quantity separately. Linear impact is a hypothesis, not a law.

Validate in sequence: hand-calculated simulator case; quote/book replay with latency and queue assumptions; calibration on separate orders; then frozen-cost strategy evaluation with conservative sensitivity and capacity analysis.

## Failure modes

- Bar touch creates impossible fills without queue priority/depth.
- Cost model calibrated on claimed-alpha trades.
- Arrival benchmark and fill clocks mismatch.
- Average cost masks volatility/liquidity dependence.
- Simulated fill is treated as proof of future execution.

## Falsifiable exercise

Freeze predicted shortfall on a held-out order set. Compare bias/error against spread-only baseline in predeclared size and volatility buckets. Reject the model for strategy evaluation if it underpredicts realized costs or the net edge fails under an upper cost bound.

## Graded sources

- **Grade 1, market-impact model review:** Gatheral (2010), “No-Dynamic-Arbitrage and Market Impact.” [DOI](https://doi.org/10.1080/14697680903373692). Model consistency result; empirical calibration remains market-specific.
- **Grade 1, execution model:** Obizhaeva & Wang (2013), “Optimal Trading Strategy and Supply/Demand Dynamics.” [DOI](https://doi.org/10.1016/j.finmar.2012.09.001). Model assumptions require local validation.
- **Grade 1, official measurement resource:** SEC Trading Markets FAQ / Rule 605 resources. [SEC page](https://www.sec.gov/rules-regulations/staff-guidance/trading-markets-frequently-asked-questions). Reporting definitions do not supply a full strategy-specific cost model.

Related: [[Microstructure exercises]] · [[High-frequency data research]] · [[Statistical inference for trading]]
