# Equities

## Instruments and structure

Equities are venue-listed ownership claims with corporate actions, trading sessions, auctions, halts, short-sale and borrow constraints, and a changing issuer universe.

## Data requirements

Use point-in-time constituents and identifiers, delisted securities, split/dividend handling, earnings publication timestamps, restatements/vintages, borrow availability/cost, and venue/session-specific execution data. Adjusted prices can be useful for returns but may leak future corporate actions if not constructed with care.

### Official source leads

- [SEC EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces): submission histories and XBRL facts; API JSON updates as filings disseminate. Use accession/acceptance timestamps and retain amendments.
- [Nasdaq Trader daily files](https://www.nasdaqtrader.com/Trader.aspx?id=DailyMarketFiles): annual CSV/TXT aggregate market statistics for Nasdaq securities, including consolidated volume regardless of venue; not tick data.
- [NYSE TAQ historical](https://www.nyse.com/market-data/historical): exchange-specific order-book/trade products and consolidated Daily TAQ; terms and coverage vary by feed.
- [FINRA short interest](https://www.finra.org/finra-data/browse-catalog/equity-short-interest): twice-monthly positions with publication lag; current corrected history only.

See [[Financial data source directory]] for timing, access, and limitations.

For the distinction between public exchange pages, delayed quote displays, and licensed executable histories, see [[Sources/Cross-market reference prices and public market data]].

## Research angles

Cross-sectional characteristics, event reactions, order flow, liquidity, analyst/filing/news data, index rebalances, corporate actions, and equity-option relationships.

## Return and universe construction

Distinguish price return from total shareholder return: dividends, splits, spin-offs, rights, mergers, delisting proceeds, and cash distributions affect investor wealth. Vendor-adjusted prices can embed corporate-action information not available at earlier timestamps; retain raw prices and event records, and construct the historical return series with explicit effective/announcement/payment dates.

Use point-in-time security identifiers and membership. Ticker is not a stable key; map issuer, share class, listing, and security through mergers, renames, and reincorporations. A current index constituent list creates survivorship and look-ahead bias. Include delisted and bankrupt firms, with their final returns and actual availability.

## Filing event example

For a filing-based signal, use SEC acceptance/dissemination timestamp to determine earliest public availability, not fiscal-period end or vendor ingestion date. Parse amendments separately and preserve the original filing version. Define whether after-hours filings enter the next regular session, account for concurrent earnings/news, and use executable prices after the information could be processed. Accounting facts can be restated and share-based units may change; validate facts and units against filing context.

## Shorting and capacity

Short-sale backtests need point-in-time borrow availability, borrow fee, recall risk, locate constraints, dividends owed, and short-sale rules. A signal with attractive long-short spread may not be implementable symmetrically. Capacity depends on turnover, market depth, participation, auction/venue choice, and impact—not just average dollar volume.

## Links

[[ETFs]] · [[Options]] · [[Market microstructure]] · [[Execution costs and market impact]] · [[Order book data and event-time reconstruction]] · [[Market data]] · [[Overfitting controls]] · [[London Strategic Edge]]
