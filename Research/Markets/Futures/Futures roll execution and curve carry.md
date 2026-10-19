# Futures roll execution and curve carry

Parent: [[Futures]]. Related: [[Commodities]], [[Fixed Income]].

## Contract holding versus curve exposure

Actual P&L for a fixed contract is multiplier times price change, adjusted for currency and contract-specific settlement. A constant-maturity strategy must state weights in listed contracts and roll schedule. For adjacent maturities, calendar spread is deferred minus nearby (state order); contango/backwardation labels and “roll yield” depend on this sign and weighting. A continuous back-adjusted series is synthetic, not a holdings ledger.

## Example

Hold one contract with multiplier $50/point: price moves 100 to 102, P&L is $100. To roll, sell nearby at 102 and buy deferred at 104; spread cost is 2 points, or $100 before fees/impact. Subtracting that gap from a back-adjusted historical chart is not itself the realized roll return: realized P&L depends on subsequent deferred-contract movement and actual roll fills.

## Fields and clock

Exchange, root and contract code, expiry/first notice/last trade/delivery dates, multiplier, tick, settlement, session/holiday, price limits, individual contract trades/quotes/volume/open interest, both roll legs and fills, roll trigger and timezone, fees, margin/collateral return, and price-adjustment methodology. For constant maturity retain explicit daily contract weights and rebalance timestamp. Avoid notice/delivery exposure unless intended.

## Failure modes

Treat front-month price changes as spot returns; use volume crossover without execution modeling; back-adjust then calculate trade P&L; ignore calendar spread bid/ask and liquidity migration; roll on expiry after liquidity has vanished; overlook delivery/notice, limits, holidays and collateral; annualize curve slope as guaranteed carry.

## Falsifiable exercise

Specify a roll rule (e.g. fixed business days before first notice), contract weights and cost model before testing one market. Reconstruct daily holdings from raw contract bars and both-leg spreads; compare back-adjusted proxy against ledger P&L. Vary roll date by a narrow predeclared band and costs by observed spread quantiles. This validates measurement, not a return premium.

## Source leads

- CME Group, contract specifications and settlements (official exchange; grade 1 for listed contract conventions, current; product-specific and may not provide unrestricted historical tick data): https://www.cmegroup.com/markets.html .
- CFTC, Commitment of Traders (official release calendar/data; grade 1 for report schedule and definitions, current; positions Tuesday, publication generally Friday, aggregated and lagged): https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm .
