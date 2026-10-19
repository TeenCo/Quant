# Forex

## Instruments and structure

Forex is a fragmented, predominantly over-the-counter market organized around currency pairs. Research must state quote convention, venue/feed, session, rollover, holiday calendar, and whether the instrument is spot, forward, future, or CFD.

## Data considerations

There is no universal consolidated spot FX tape or volume. Bid/ask, venue-specific prints, broker candles, swaps/roll, and indicative quotes have different semantics. Validate spreads, timestamp timezone, daylight saving, weekend gaps, and stale values. Check contract sizing and pip/point conventions.

Official reference-rate sources such as the [ECB](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html) or [Bank of England database](https://www.bankofengland.co.uk/boeapps/database/) are useful for macro/valuation context but are not executable spot quotes. BIS bilateral/effective exchange-rate series are useful for broad currency context; none constitutes a consolidated FX order book.

For cross-country macro and published FX reference-rate leads, see [[Sources/Global macro and national statistics sources]] and [[Sources/Cross-market reference prices and public market data]].

## Research angles

Carry and forward premia, momentum/reversal, macro releases and surprises, central-bank communication, cross-currency basis, session/holiday effects, volatility and liquidity regimes, order-flow proxies, and relative value across currency baskets.

## Pair conventions and return construction

For a pair \(A/B\), the quote is units of currency B per unit of A. If the quote rises, A appreciates relative to B under that convention. A long position's return depends on direction, notional currency, conversion, and financing. Validate signs with a small hand-calculated example before building a basket.

Spot return alone omits the interest differential/roll. Under covered interest parity in idealized conditions, forward points relate to the two money-market rates and tenor; actual tradable returns can differ because of cross-currency basis, collateral, credit, capital constraints, and execution. Distinguish spot-price momentum from total return including swap/forward carry, and use point-in-time tradable rates and rollover conventions.

## Example hypothesis: release-time FX surprise

Predefine one scheduled release, pair, surprise measure (actual minus a licensed point-in-time consensus, normalized by historical surprise scale), event timestamp, and short post-release horizon. Use the first executable quote after the release plus a realistic latency, not a daily bar close that may include future price movement. Control for simultaneous releases, surprise correlation, session liquidity, spread widening, and event clustering. A same-day central-bank rate series is not an intraday executable price series.

## FX-specific controls

- Treat OTC venue quotes as samples of fragmented liquidity; vendor volume is not global volume.
- Normalize day boundaries with daylight-saving-aware calendars; New York close and UTC day bars differ.
- Include rollover triple-charge/holiday rules and financing for multi-day positions.
- Separate spot, deliverable forward, NDF, futures, and CFD products; their basis, access, and settlement differ.
- For cross rates, reconcile triangular quotes after timestamp and spread alignment; apparent arbitrage can be asynchronous or non-executable.

## Methods and links

[[Time series]] · [[Causal inference]] · [[Market microstructure]] · [[Order book data and event-time reconstruction]] · [[Execution costs and market impact]] · [[Edge validation]] · [[Market data]] · [[London Strategic Edge]]

## Initial data lead

LSE's public SDK lists FX and historical candles as available. Treat coverage and feed characteristics as provider claims; inspect actual catalog spans and independently validate samples.
