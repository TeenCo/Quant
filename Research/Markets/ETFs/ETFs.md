# ETFs

## Instruments and structure

Exchange-traded funds hold or reference baskets, indexes, commodities, currencies, or other assets. A quoted ETF share price, intraday indicative value, net asset value, creation/redemption activity, and underlying basket are related but distinct.

## Data considerations

Account for distributions, splits, premium/discount to NAV, stale underlying prices across time zones, index changes, fund closures, liquidity, creation/redemption, fees, and historical holdings availability. Survivorship bias is material when only current funds are studied.

Historical constituent/holdings and corporate-action vintages should be retained; current ETF holdings cannot stand in for historical holdings without a point-in-time source.

## Research angles

Premium/discount dynamics, flow/creation effects, cross-ETF relative value, basket liquidity, event and rebalance effects, leveraged/inverse compounding, and ETF/underlying lead-lag relationships.

## NAV, indicative value, and premium/discount

An ETF's exchange price is formed by trading; NAV is calculated from fund assets/liabilities under a valuation policy. Intraday indicative values may use stale or asynchronous underlying prices, especially for foreign securities or less-liquid assets. A measured premium/discount can therefore reflect price discovery across market hours, stale marks, basket hedging costs, or a genuine dislocation. Record each source's timestamp and valuation method before interpreting it.

Creation/redemption arbitrage can help align price with basket value, but it is not frictionless or guaranteed. Authorized participant capacity, basket composition, financing, borrow, taxes, settlement, and market stress affect the mechanism. Historical holdings and creation baskets may be unavailable or revised; current holdings cannot substitute for point-in-time exposure.

## Leveraged/inverse compounding example

For a daily-reset leveraged ETF with target multiple \(L\), a simplified daily gross return is approximately \(L r_t\), before fees/financing/tracking error. Over two periods, wealth is \((1+Lr_1)(1+Lr_2)\), not \(1+L(r_1+r_2)\). With index returns +10% then -9.09%, the index returns approximately to its starting level, but a 2x daily product yields \(1.20\times(1-0.1818)\approx0.982\), a loss before costs. This path dependence makes horizon and rebalancing essential in backtests.

## ETF-specific research checklist

Use point-in-time fund universe (including closures/mergers), distributions and split-adjusted total returns, actual holdings/baskets when available, underlying market hours, premium/discount methodology, expense ratio, securities lending/cash drag, and venue-specific executable quotes. Model creations/redemptions only if the required data and participant access are represented.

## Links

[[Equities]] · [[Market microstructure]] · [[Execution costs and market impact]] · [[Market data]] · [[Edge validation]] · [[London Strategic Edge]]
