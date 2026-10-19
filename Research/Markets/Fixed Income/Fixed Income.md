# Fixed Income

## Instruments and structure

Fixed income spans sovereign and corporate bonds, money markets, swaps, credit derivatives, and yield curves. Price/yield conventions, coupon schedules, accrued interest, duration, convexity, collateral, and settlement matter.

## Data considerations

Distinguish executable quotes, evaluated prices, transaction prints, and benchmark rates. Check stale pricing, liquidity, rating changes, default/recovery, callability, roll-down, curve construction, and revision/release history for macro/rate data.

Public source leads include the [FINRA Data Catalog](https://www.finra.org/finra-data/browse-catalog) for selected fixed-income aggregates and TRACE activity, and [BIS statistics](https://data.bis.org/) for international banking, debt securities, derivatives, and global-liquidity aggregates. Transaction-level TRACE history and academic access have separate agreements, delays, and fees; see [[Financial data source directory]].

For Treasury Fiscal Data, ECB SDMX, and additional BIS access/field distinctions, see [[Sources/Cross-market reference prices and public market data]].

## Research angles

Curve carry/roll, term premia, duration/convexity, credit spread, liquidity, policy and inflation surprises, issuance/auction effects, and cross-market relative value.

## Bond price sensitivity: duration and convexity

For a small yield change \(\Delta y\), a bond's approximate percentage price change is

\[
\frac{\Delta P}{P}\approx -D_{mod}\Delta y+\frac{1}{2}C(\Delta y)^2,
\]

where modified duration \(D_{mod}\) is local first-order sensitivity and convexity \(C\) captures second-order curvature. This approximation assumes a parallel yield shift and small moves; key-rate durations are more suitable when curve shape changes. Cash-flow, option, and spread effects can invalidate a simple duration hedge.

## Curve construction and timing

Zero curves, par yields, swap curves, and benchmark yields are different objects with conventions and instrument sets. Record input quotes, bootstrapping method, day count, compounding, collateral/discounting framework, and release/market timestamp. A published daily curve may be an evaluated end-of-day measure, not a tradable quote at every historical decision time.

## Credit and liquidity decomposition

Corporate yield spreads can combine expected default losses, risk compensation, liquidity, tax, embedded options, and measurement differences. A spread change is not a pure default-probability update. TRACE prints are transactions with reporting/access features, while evaluated bond marks may be model-based and stale. For illiquid bonds, stale pricing can mechanically smooth returns and understate measured volatility/correlation; flag quote age and compare with transaction evidence where available.

## Fixed-income event example

For a scheduled policy announcement, define the instrument (cash Treasury, futures, swap), contract/tenor, event timestamp, pre-event quote window, and post-event executable window. Separate level, slope, and curvature exposures; avoid attributing an entire curve move to one policy surprise when simultaneous macro news and term-premium changes are possible. Include futures CTD/basis and roll if using Treasury futures.

## Links

[[Economics]] · [[Time series]] · [[Futures]] · [[Market microstructure]] · [[Market data]] · [[London Strategic Edge]]
