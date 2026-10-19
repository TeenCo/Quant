# Futures

## Instruments and structure

Futures are standardized contracts with expiry, tick size/value, margin, settlement, and exchange rules. Continuous series are constructed by rolling contracts and are not themselves directly tradable.

## Data considerations

Preserve individual contract prices and volume/open interest. Document roll date/rule, calendar vs. cash settlement, back-adjustment, limit moves, trading sessions, holidays, and delivery constraints. Avoid assuming a back-adjusted continuous series represents executable price history.

## Research angles

Term structure/carry, roll yield, momentum, positioning (including COT), calendar spreads, basis, inventory/supply data, and event risk.

The [CFTC COT release](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm) reports Tuesday positions, generally released Friday at 3:30pm ET. This is a lagged, aggregated positioning measure with reporting thresholds and category definitions; align features to the Friday release time, not the Tuesday as-of date.

See [[Sources/Cross-market reference prices and public market data]] for COT fields/report variants and the commercial access boundary for CME/DataMine history.

## Contract return and roll decomposition

A futures position's P&L is determined by changes in the held contract price and contract multiplier, not by a synthetic continuous series. A backtest that holds a constant-maturity exposure must specify how it rolls between expiries, including both legs' fills, calendar spreads, liquidity, and roll dates. Back-adjustment is a visualization/analysis convention; it changes historical price levels and does not represent an executable contract path.

For a commodity, the nearby/deferred price difference can reflect storage, financing, convenience yield, seasonality, quality/location, and delivery constraints. “Roll yield” labels are methodology-dependent and should not be confused with guaranteed return. Keep price return on each held contract separate from roll/trading costs and collateral return.

## Positioning and open interest

COT categories are aggregated reports with definitions, thresholds, and reporting delays. They do not identify individual traders' motives or exact hedging exposures. A Tuesday position snapshot released Friday cannot be used earlier than Friday's public release (and a strategy may need further processing delay). Normalize changes only with a strictly backward-looking history; account for contract-specific scaling, report type, and revisions/corrections.

## Contract lifecycle checklist

Store contract code, first/last trade date, notice/delivery dates, settlement type, multiplier, tick, price limits, session, expiry calendar, and roll rule. Avoid holding into delivery unless that is the intended physical process. For spread research, preserve both legs and ensure synchronized tradable prices.

## Links

[[Commodities]] · [[Fixed income]] · [[Time series]] · [[Market microstructure]] · [[Execution costs and market impact]] · [[Market data]] · [[London Strategic Edge]]
