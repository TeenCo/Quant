# ETF NAV, creation and basket mechanics

Parent: [[ETFs]]. Related: [[Equities]], [[Market microstructure]].

## Mechanics and measures

NAV per share at valuation time is (assets less liabilities)/shares outstanding. Premium/discount = market price / NAV - 1; use synchronized valuation timestamps and consistent share class/currency. Authorized participants (APs) deliver a creation basket plus cash for creation units, or return units for redemption, under fund terms. Arbitrage capacity is conditional on basket hedgeability, financing, borrow, fees, taxes, settlement and AP balance sheet; the mechanism does not guarantee instant convergence.

## Example

Suppose ETF bid/ask is 100.08/100.12, published NAV 100.00, and underlying foreign shares last traded before the ETF session. Naively midpoint premium is 0.10%; it is not a tradable 10bp arbitrage: stale foreign marks may understate current fair value, while hedge, FX, basket and creation costs may exceed the gap. If a synchronized executable basket estimate is 100.09, the comparable midpoint gap is only 1bp.

## Data fields and clock

Retain fund/share class, holdings and creation basket with publication timestamp and version, cash component, shares outstanding, NAV valuation time/policy, market bid/ask/size/trades, iNAV methodology/time, underlying venue/session and quote age, FX, distributions, corporate actions, fees, settlement cycle, creation-unit size, AP eligibility, and holiday calendar. Differentiate fund holdings from daily PCF/creation basket. Preserve archived point-in-time files; current holdings are not historical truth.

## Failure modes

Use asynchronous NAV and ETF quotes; treat iNAV as executable; infer AP capacity from price convergence; omit foreign-market closures, fair-value marks, distributions, taxes and settlement; use current basket retrospectively; ignore premium persistence caused by underlying price discovery; count stale marks as arbitrage.

## Falsifiable exercise

For one cross-listed or foreign-underlying ETF, compare US-session ETF returns/premium changes against next-open underlying price discovery, controlling for FX and market-hours overlap. Freeze source timestamps and premium construction; exclude stale days by a predeclared quote-age threshold. If gaps predict executable convergence after spread/hedge costs in a later sample, report that as a result to replicate, not presumed alpha.

## Source leads

- SEC, Investor Bulletin: Exchange-Traded Funds (official investor explanation; grade 2 for structure, current page, moderate novelty; not a detailed AP dataset): https://www.sec.gov/investor/alerts/etfs.pdf .
- 17 CFR 270.6c-11 (official rule; grade 1 for US legal mechanics, 2019/current codification, low novelty; jurisdiction-specific, consult fund prospectus): https://www.ecfr.gov/current/title-17/chapter-II/part-270/section-270.6c-11 .
- ICI ETF resource center (industry source; grade 4, updated resource, lower novelty; advocacy/industry framing and not independent performance evidence): https://www.ici.org/etf .
