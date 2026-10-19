# Order Book Data and Event-Time Reconstruction

An order book is a venue-specific queue of displayed buy and sell interest, typically organized by price and priority rules. Historical reconstruction is only valid when the researcher understands exactly what each message records and how the feed was captured.

## Data representations

- **Level 1 / top of book:** best bid/ask and possibly sizes; low dimensional but hides depth beyond the inside quote.
- **Market-by-price (aggregated depth):** total displayed size at price levels, but not individual queue position.
- **Market-by-order:** individual order events and identifiers where supplied; can support queue reconstruction but may omit hidden/auction interest.
- **Snapshots:** periodic states; may miss intervening events and queue changes.
- **Incremental event feeds:** adds, modifies, cancels, executions, auction messages, and status changes. Requires correct sequence and recovery logic.

## Reconstruction sequence

1. Preserve raw messages, original timestamps, exchange sequence numbers, receive timestamps, and venue identifiers.
2. Identify snapshot-to-event replay rules, message types, sequence reset behavior, corrections, and recovery gaps.
3. Apply events in sequence and validate book invariants: nonnegative displayed size, valid side/price, crossed-book handling, and expected tick increments.
4. Retain both event time and local receive time; clock drift and feed latency affect any simulated decision.
5. Model session opens/closes, auctions, halts, trading status, and market-specific phases explicitly.
6. Record whether data are consolidated across venues or venue-specific; do not infer a consolidated NBBO or global queue from one feed.
7. Validate reconstructed states against provider snapshots or independent observations and summarize dropped/duplicated messages.

## Timestamp and sampling traps

- Exchange event time, vendor timestamp, receive time, bar-open time, bar-close time, and decision time are different quantities.
- Timestamps may have coarse resolution or ties; never assume stable ordering without sequence fields.
- Snapshot compression or vendor filtering can alter apparent event intensities and queue turnover.
- Quote updates can be cancellations, repricing, or additions; top-of-book imbalance alone does not reveal participant intent.
- Trade signing from quotes is error-prone when quotes are stale, locked/crossed, or fragmented.

## Feature ideas (research leads, not validated signals)

Depth imbalance, queue depletion/replenishment, cancellation intensity, order-flow imbalance, spread/depth resiliency, event clustering, and trade/quote response may forecast short-horizon price or fill outcomes. Test out of time and venue, compare with simple baselines, account for feed latency and multiple feature search, and evaluate executable net value.

## Reconstruction invariant example

For a price-level book, maintain displayed quantity \(q_{p,s}\ge0\) for each price \(p\) and side \(s\). An add increases quantity; a cancel/reduction decreases it; an execution reduces or removes resting quantity according to the feed's message semantics. A snapshot reset replaces state at a known sequence, after which only subsequent ordered events should be applied. A gap in sequence invalidates later state until recovery logic supplies a valid snapshot/replay. Keep raw messages and a deterministic event log so every state can be rebuilt.

Check event count by type, sequence continuity, duplicate IDs, nonnegative size, tick-grid validity, crossed/locked states, and matching with venue snapshots. Unexpected crossed books may be real during transitions or a parsing error; inspect timing and rule documentation rather than silently deleting rows.

## Latency alignment

For a feature computed from event time \(t_e\), the decision cannot occur before receive/processing time \(t_r\) plus compute/route latency. Backtests should use the information set at that decision time, not the exchange timestamp alone. When clock synchronization uncertainty is comparable to the prediction horizon, describe a latency interval and test conservative delays. Cross-venue lead-lag results require clock alignment and should survive deliberate timestamp perturbation within plausible error bounds.

## Connected notes

[[Market microstructure]] · [[Execution costs and market impact]] · [[Order flow and event models]] · [[Market data]] · [[Statistical inference for trading]] · [[Equities]] · [[Futures]] · [[Crypto]]
