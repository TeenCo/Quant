# High-Frequency Market Data Research

High-frequency data can expose intraday liquidity, event dynamics, and execution effects invisible in daily bars. It also amplifies timestamp errors, microstructure noise, dependence, data-volume costs, and multiple-testing risk.

## Start from the observation process

Specify what generates each row: trade, quote, book update, auction event, or vendor-aggregated bar. Preserve event and receive timestamps, sequence numbers, venue, instrument, and data-filter definitions. A “tick” is provider-specific and must not be treated as a universal primitive.

## Research questions

- Does an imbalance or event-intensity feature forecast mid-price changes after the available latency?
- Are quotes replenished after a market order, and how does resiliency vary by regime/depth?
- Does order-flow clustering persist after accounting for time-of-day and common news?
- How does execution shortfall change with urgency, participation, spread, and volatility?
- Are cross-venue effects genuine lead-lags, or clock/aggregation/fragmentation artifacts?

## Necessary controls

- Maintain quote/trade ordering and clock conventions.
- Treat locked/crossed/stale quotes and ambiguous trade signing explicitly.
- Use event or time bars consistently; control for intraday seasonality.
- Use block/bootstrap or other uncertainty methods that respect serial and cross-event dependence.
- Prevent label overlap and feature leakage around decision timestamps.
- Use chronological holdouts and report all explored features, depths, horizons, event filters, and thresholds.
- Include fees, spread, rebates, queue position, partial fills, impact, latency, and capacity.

## Efficient computing

Columnar storage, time/venue partitions, predicate pushdown, chunked processing, event-driven rather than repeated full-book recomputation, and incremental rolling features can save runtime. Validate reconstructed outputs against a simple reference implementation before optimizing. See [[Performance]] and [[Research pipelines]].

## Reading leads

- [[Sources/Obizhaeva Wang 2005]] — dynamic liquidity and execution.
- [[Sources/Bacry Mastromatteo Muzy 2015]] — Hawkes processes in finance.
- [[Order book data and event-time reconstruction]] · [[Execution costs and market impact]] · [[Order flow and event models]]
- [[Execution cost validation protocol]]
