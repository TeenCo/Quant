# Crypto

## Instruments and structure

Crypto markets include spot assets, centralized exchanges, decentralized venues, perpetual swaps, dated futures, and options. Each venue has distinct market hours, matching rules, settlement, fees, liquidation, custody, and data quality.

## Data considerations

Specify venue, pair/base/quote, contract multiplier, token migration, chain, timestamp, and source. Volume is fragmented and may be distorted; outages, delistings, wash activity, forks, airdrops, funding, and liquidation events require explicit treatment. Include exchange failure and custody risk in universe definitions.

Exchange REST/WebSocket feeds (e.g., [Kraken public OHLC documentation](https://docs.kraken.com/api/docs/rest-api/get-ohlc-data)) are venue-specific. Kraken documents that OHLC returns at most the most recent 720 entries and includes a current, uncommitted candle; do not assume it is an unlimited historical archive or use the final incomplete candle as a finalized bar.

See [[Sources/Cross-market reference prices and public market data]] for field/timestamp details and the snapshot-versus-stream distinction for Kraken and Coinbase.

## Research angles

Funding and basis, spot/perpetual lead-lag, cross-venue spreads, order-book liquidity, volatility regimes, on-chain activity, network congestion, stablecoin flows, protocol events, and listing/unlock schedules.

## Perpetual funding and basis

Perpetual swaps use periodic funding transfers between long and short positions to help anchor contract price to an index/spot reference. Funding is a cash flow, not a guaranteed yield: it varies by venue and timestamp, may be capped or formula-dependent, and co-moves with leverage demand and stress. A spot/perpetual carry backtest must align funding settlement times, contract multipliers, collateral currency, borrow/financing, fees, mark/index definitions, liquidation rules, and outages.

## Cross-venue arbitrage is an execution problem

Observed price divergence across exchanges is not directly realizable unless the trader can access both venues, hold/transfer collateral, execute both legs, and manage funding, inventory, withdrawal delays, and venue credit risk. Synchronize quotes and account for queue/latency; include failed fills and exchange downtime. A strategy should not assume instantaneous transfers to repair inventory.

## On-chain data clocks and entity attribution

Blockchain event time, block inclusion time, finality/confirmation time, node observation time, indexing time, and vendor publication time are distinct. Reorganizations can alter canonical history; entity labels may be retrospective and proprietary. Preserve chain/block/transaction identifiers and raw observations, record confirmation policy, and avoid applying current wallet labels historically without a point-in-time archive. On-chain quantities can be hard to interpret as economic ownership or intent.

## Minimum venue-aware contract schema

Record venue, instrument type, symbol, base/quote/margin currencies, multiplier, tick/lot, funding formula and settlement time, index/mark price, expiry, settlement/collateral, fee tier, liquidation rules, and status history. Normalize returns only after contract payoff and currency conversion are explicit.

## Links

[[Market microstructure]] · [[Order book data and event-time reconstruction]] · [[Order flow and event models]] · [[Execution costs and market impact]] · [[Time series]] · [[Alternative data]] · [[Edge validation]] · [[Market data]] · [[London Strategic Edge]]
