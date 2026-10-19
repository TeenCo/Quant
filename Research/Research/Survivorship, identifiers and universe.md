# Survivorship, Identifiers, and Historical Universes

## Survivorship bias

If a study includes only securities that exist today, it omits delisted, bankrupt, acquired, renamed, or otherwise inactive securities. Performance can be biased upward and risk understated. A historical test requires the universe as it existed at each date, including securities that subsequently disappeared.

## Identifier hygiene

Tickers are labels, not durable entity keys. They can change, be reused, differ by venue, or represent multiple share classes. Maintain mappings among stable identifiers (e.g. CIK for SEC filers, FIGI/ISIN where licensed, exchange/vendor IDs), ticker, venue, and effective dates.

## Corporate actions and security lifecycle

Record splits, dividends, spin-offs, mergers, ticker changes, bankruptcies, trading suspensions, IPOs, listing/delisting dates, and contract expiries. Distinguish raw tradable prices from retrospectively adjusted series. Adjustments should not leak an event before its effective/publication time.

## Constituents and classification drift

Index membership, sector classifications, industry codes, and instrument coverage change. Current membership applied to historical data creates look-ahead. Preserve historical constituents and classification vintages; record methodology changes and missing coverage.

## Universe test checklist

- Was the security eligible and tradable at the simulated time?
- Are delisted firms/contracts retained through their final observable outcome?
- Are identifiers stable and mappings effective-dated?
- Are missing prices due to no trade, halt, vendor gap, or delisting?
- Does the strategy depend on a liquidity/price screen calculated with future values?
- Are shortability, borrow, margin, and market access represented realistically?
- Are results robust to reasonable historical-universe and corporate-action definitions?

## Effective-dated mapping example

Maintain a mapping table with stable security ID, ticker, venue, share class, `valid_from`, `valid_to`, and source/version. A query for date \(t\) selects mappings satisfying `valid_from <= t < valid_to`, rather than joining on current ticker. Treat issuer-level identifiers and security-level identifiers separately: one issuer can have multiple listed securities, depositary receipts, or share classes with different tradability and returns.

## Delisting and missing terminal outcomes

Distinguish a missing vendor record, a trading halt, a delisting, merger consideration, bankruptcy recovery, and a security that never traded in the interval. Delisting returns can be large and are often missing in incomplete databases. If the terminal outcome is unknown, flag it and bound sensitivity rather than dropping the name or assuming a zero return. Universe filters (price, liquidity, exchange, market cap) must be computed from values available at the historical decision time.

## Connected notes

[[Equities]] · [[ETFs]] · [[Futures]] · [[Options]] · [[Crypto]] · [[Data provenance and point-in-time]] · [[Feature engineering]] · [[Overfitting controls]]

See also [[Historical-universe reconstruction and delisting outcomes]] for a worked universe comparison.
