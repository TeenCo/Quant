# Market Microstructure, Execution, and Liquidity

Market microstructure studies how trading mechanisms, information, inventory, and order flow generate prices and execution outcomes. It links a statistical forecast to the price and quantity actually obtainable.

## Topics

- Limit order books, market/limit orders, queue priority, matching rules.
- Bid/ask spread, depth, resiliency, adverse selection, inventory risk.
- Price impact, temporary/permanent impact, slippage, execution scheduling.
- Venue fragmentation, auction mechanisms, dark pools, latency, and market data definitions.
- Tick size, trading hours, halts, funding, margin, and short-sale constraints.
- [[Order book data and event-time reconstruction]] — event feeds, snapshots, sequence, and synchronization.
- [[Execution costs and market impact]] — implementation shortfall and capacity-aware evaluation.
- [[Order flow and event models]] — point processes, Hawkes processes, and order-flow imbalance.

## Edge implications

Backtest marks are not fills. Use executable prices and realistic order timing, include costs/impact and capacity, and test whether a signal survives after the delay required to act. Compare market-specific microstructure across [[Forex]], [[ETFs]], [[Crypto]], [[Equities]], [[Futures]], and [[Options]].

[[Sources/Bacry Mastromatteo Muzy 2015]] introduces a broad review lead on Hawkes/point-process models for transactions, order books, and execution. [[Sources/Obizhaeva Wang 2005]] studies how supply/demand replenishment changes optimal execution. See [[Sources/Hawkes processes lead]] for candidate tests and identification cautions.

## Spread, impact, and price formation

The quoted spread is the difference between best ask and best bid; the midpoint is a reference mark, not an executable price. A market order typically pays the spread and may walk depth. A limit order avoids crossing only if it fills; fill probability, queue position, adverse selection, and opportunity cost are part of its economics. Distinguish temporary impact (which may decay) from persistent price impact; empirical decomposition depends on horizon and benchmark.

## Order-flow imbalance example

At the best quotes, a simple signed update can combine changes in bid/ask prices and displayed sizes into an order-flow imbalance measure. Its short-horizon association with mid-price changes may reflect mechanical book depletion, information, or both. Evaluate at the timestamp when the message could be received, apply realistic latency, compare to lagged returns/spread/depth baselines, and test whether the predicted move exceeds spread/fees/impact. One venue's displayed depth omits hidden liquidity and other venues.

## Queue and adverse-selection tradeoff

A passive order earns spread/rebate only conditional on being filled; fills are not random. The order may be most likely to execute precisely when the market is moving against it. Therefore, backtests that fill whenever price touches a limit price without queue or subsequent price-path modeling can overstate passive-order value. Report fill probability and conditional post-fill markout separately, and include cancellations, partial fills, and priority rules.
