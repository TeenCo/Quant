# Execution Costs and Market Impact

Execution cost is the difference between the economic decision price and the realized execution outcome. It can consume or reverse a small forecast edge. A credible backtest must model decisions and fills, not just signals and closing prices.

## Cost components

- **Spread:** crossing from a reference/mid price to an executable bid/ask.
- **Fees and rebates:** venue, clearing, broker, and maker/taker charges.
- **Slippage:** movement between signal/decision and fill, including latency and partial fills.
- **Market impact:** price response to the order itself; depends on size, liquidity, urgency, volatility, and information.
- **Opportunity cost:** unfilled quantity, missed price movement, or queue loss.
- **Financing and constraints:** funding, borrow, margin, roll, and capital use.

## Implementation shortfall

Compare the realized execution path against a pre-specified decision benchmark (such as arrival price or an agreed decision-time reference). Decompose filled costs, unfilled opportunity costs, fees, and market movement carefully. The benchmark must be selected before observing execution outcomes; otherwise the evaluation can be biased.

## A simple capacity-aware workflow

1. Define signal time, decision time, order type, size, urgency, and benchmark.
2. Estimate spread and depth from point-in-time quote data at decision time.
3. Simulate order arrival latency and fill probability/partial fills using the market's matching rules.
4. Estimate impact as a function of participation, volatility, depth, and horizon; show a range rather than a single false-precision value.
5. Include fees, borrow, funding, and venue effects.
6. Recompute portfolio returns net of implementation shortfall and opportunity cost.
7. Stress costs upward and report break-even costs/capacity.

## Model risks

Cost estimates are often endogenous: informed flow selects when to trade, liquidity providers change quotes, and the strategy itself changes market state. A model calibrated to small orders may not extrapolate to larger size. Auction, OTC, fragmented, and crypto markets differ materially.

## Implementation-shortfall accounting example

For a buy order with decision benchmark \(P_0\), filled quantities \(q_i\) at prices \(P_i\), and unfilled quantity \(Q_u\), a simplified signed shortfall is

\[
IS=\sum_i q_i(P_i-P_0)+Q_u(P_T-P_0)+\text{fees},
\]

where \(P_T\) is a pre-specified opportunity-cost mark at the evaluation horizon. Reverse signs for sells or define a signed direction variable. This decomposition is sensitive to benchmark and terminal-mark choices; set both before examining outcomes and report filled and unfilled components separately. For a portfolio, aggregate in consistent currency and normalize by notional only after handling FX and contract multipliers.

## Impact curve and capacity sensitivity

Estimate costs across order size/participation buckets and market states, with uncertainty intervals. A common empirical form relates impact to volatility, participation rate, and liquidity, but functional forms (linear, square-root, transient) are model hypotheses, not universal laws. Validate on held-out executions and show break-even alpha versus size. Do not extrapolate a low-size calibration without stressing nonlinearity, crowding, and changed market response.

## Source lead

[[Sources/Obizhaeva Wang 2005]] models dynamic supply/demand replenishment and finds that execution timing and discrete/continuous trading choices depend on book dynamics in its model. It is a foundational, older theoretical study; its exact prescriptions should not be transferred mechanically to modern venues.

## Connected notes

[[Market microstructure]] · [[Order book data and event-time reconstruction]] · [[Edge validation]] · [[Research workflow]] · [[Forex]] · [[ETFs]] · [[Crypto]] · [[Equities]] · [[Futures]] · [[Options]]
