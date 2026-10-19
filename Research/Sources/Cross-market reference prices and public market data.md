# Cross-market reference prices and public market data

Review date: 2026-10-18. This is a gap-focused companion to [[Financial data source directory]], whose existing entries already cover FRED/ALFRED, BLS, BEA, BIS/ECB at overview level, CFTC COT, CME historical products, NYSE TAQ, Cboe aggregate options statistics, Nasdaq daily files, Kraken OHLC, and Coinbase candle API. This note adds actionable detail and identifies the boundary between official reference series and executable market observations.

**Evidence grades (1 strongest, 10 weakest)** grade documentation claims only. Official primary source documentation and data descriptions are generally 1; exchange product pages 1 for product existence/access description, not value-for-money/completeness; venue-provider API documentation 5 for coverage/behavior pending independent checks. Recency is page review date above; individual release/data vintage may be older. Novelty is relative to the parent directory: high for specific schema/terms/point-in-time mechanics, moderate for exchange and venue endpoints. Source type is stated per source.

## How to interpret the data

- **Reference / administrative / statistical values** are official published benchmarks, rates, surveys, or aggregate reports. Authority of publication does not make a value an executable quote. A daily FX reference rate, Treasury yield curve, or weekly COT position is not a bid/offer or fill.
- **Executable market data** require instrument/venue identified trades, quotes, or order-book events with event time, receipt/publication time, condition codes, and licensing/entitlements understood. Free delayed displays and end-of-day bars support lower-frequency research, not claims about intraday fills.
- Record at minimum `event_or_reference_time`, `first_publication_time` (if established), `retrieved_at_utc`, source/endpoint, query parameters, raw payload/version, instrument identifier, and status/revision. Preserve UTC plus source-local timezone and trading date. If no historical release timestamp/vintage exists, label it latest-history-only or not point-in-time verified.

## Official reference rates and cross-border statistics

### U.S. Treasury Fiscal Data — Treasury securities and yield-curve series

- **Direct verified URLs:** [Fiscal Data API](https://fiscaldata.treasury.gov/api-documentation/) · [Daily Treasury par yield curve rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates) · [API example: average interest rates on Treasury debt](https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates).
- **What is actually published:** Endpoint `avg_interest_rates` returns `record_date`, `security_type_desc`, `security_desc`, `avg_interest_rate_amt`, `src_line_nbr`, fiscal/calendar year-quarter-month-day fields. These are average interest rates on debt outstanding by Treasury security categories, not a security-level yield or quote. Treasury daily curve page publishes constant-maturity par yields at standard maturities; separate Treasury pages expose bill rates and real yields. Check each table's own definitions/schema rather than treating them as one series.
- **Access/timing/terms:** Fiscal Data API is public, no API key; JSON/CSV and filtering, sorting, pagination. Public Treasury pages provide daily tables/downloads. Not streaming/live. Endpoint record date is a reference date; not a guaranteed timestamp the value first became available. Capture retrieval time and page/API response. Public government access does not automatically grant redistribution rights to transformed third-party content; consult published terms.
- **Limitations:** Par curve is a fitted reference curve, not executable prices; average debt costs describe outstanding portfolio, not marginal funding. Daily rates omit bid/ask, depth, on/off-the-run identity, and intraday movement. Treasury may revise/correct tables; current API history alone does not establish old publication vintages.
- **Assessment:** Grade 1, recent 2026-10-18; novelty high (distinguishes Treasury accounting average rate from market yield). Source type: U.S. government primary publication/API.

### ECB Data Portal / SDW successor — euro-area observations

- **Direct verified URLs:** [API overview](https://data.ecb.europa.eu/help/api/overview) · [API data retrieval](https://data.ecb.europa.eu/help/api/data) · [ECB euro foreign-exchange reference rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html).
- **Fields/data:** SDMX 2.1 REST service exposes disseminated ECB statistical observations and metadata; dimensions identify series (including frequency, reference area, counterpart/instrument and time as applicable), attributes explain units/status/precision. Series vary: daily reference exchange rates and yield curves, policy rates, monetary and other statistics. Discover exact DSD/dataflow and codelists before interpreting an observation; there is no single universal row schema.
- **Access/timing/terms:** Public REST and portal downloads; no API key required in the documented retrieval workflow. Statistical observations are not live order-book feeds. Reference date/time is series-specific; reference FX rates are published on working days around 16:00 CET and ECB expressly discourages transaction use. API response/retrieval timestamp is not the original publication timestamp. Check revision/status attributes and release information.
- **Limitations:** Reference levels are indicative, not executable; frequency and release lag differ by series. Revisions, breaks, unit changes and calendar conventions matter. Store complete SDMX key, DSD/version, attributes, and retrieval timestamp.
- **Assessment:** Grade 1; recent 2026-10-18; novelty moderate-high (API schema and time semantics). Source type: central-bank statistical primary source.

### BIS Data Portal — cross-country financial reference datasets

- **Direct verified URLs:** [Bulk downloads](https://data.bis.org/bulkdownload) · [API documentation](https://stats.bis.org/api-doc/v2/) · [permitted-use terms](https://data.bis.org/help/legal#terms-of-permitted-use-of-bis-statistics).
- **Fields/data:** Topic bulk archives in CSV (columnar/flat) and SDMX 2.1 formats, including bilateral/effective exchange rates, locational and consolidated banking, debt securities, credit, debt-service ratios, exchange-traded derivatives, OTC derivatives and central-bank policy rates. Dataset-specific dimensions/attributes and code lists define country, instrument, currency, maturity, unit and period; inspect metadata rather than assuming columns across topics.
- **Access/timing/terms:** Public downloads/API without an access key in the reviewed docs. Bulk page lists dataset-specific publication/update dates (e.g. bilateral exchange rates dated 15 Oct 2026 on review); these are periodic historical statistics, not live prices. Reference period and publication/update date are distinct. BIS permitted-use/copyright terms apply; cite BIS and check redistribution provisions.
- **Limitations:** Aggregates and estimates compiled from national sources, variable coverage/frequency, revisions and breaks; derivatives statistics are not contract-level quotes/trades. Bulk files are snapshots, so archive downloaded file/version and retrieval timestamp for vintage control.
- **Assessment:** Grade 1 for published metadata/access; recent 2026-10-18; novelty moderate (specific ready-to-download formats/update dates). Source type: international organization primary statistical compilation.

## Public exchange and regulator data: bars, histories, reference data

### CFTC Commitments of Traders (COT) — positioning, not price

- **Direct verified URLs:** [COT hub and report definitions](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm) · [Public Reporting Environment](https://publicreporting.cftc.gov/) · [release schedule](https://www.cftc.gov/MarketReports/CommitmentsofTraders/ReleaseSchedule/index.htm).
- **Fields/data:** Tuesday open interest and long/short/spreading positions by reportable trader category; report formats also include changes, shares of open interest, trader counts and (long reports) concentration measures. Legacy, Supplemental, Disaggregated and Traders in Financial Futures (TFF) have different universes/classification. Both futures-only and futures-plus-options combined reports exist for relevant types; TFF covers financial contracts including currencies, Treasury securities, stock indexes and VIX.
- **Access/timing/terms:** Public static reports, annual compressed files, PRE filters/downloads and API; CFTC says no API token is currently provided/usually needed, asks users not to overuse. Generally Friday 3:30pm Eastern release from prior Tuesday, subject to holidays. Data represent Tuesday, not Friday or current positions. Historical published data are not backdated/updated per CFTC FAQ. Public access; abide by site/API usage and attribution terms.
- **Limitations:** Threshold-based reporting; markets can disappear below 20 large traders; trader classes are self-reported business-purpose categories, not inferred intent. Positions aggregate and netting/spreading complicate interpretation; CFTC states suppressed trader counts below four. No price, executions, order flow, or intraday signal. Point-in-time is much better defined by release schedule, but persist actual release timestamp/calendar.
- **Assessment:** Grade 1; reviewed 2026-10-18; novelty low-moderate (parent already lists COT, this adds fields and timestamp semantics). Source type: U.S. regulator primary report.

### CME Group DataMine and real-time products — futures/options executable history (commercial)

- **Direct verified URLs:** [Browse data products](https://www.cmegroup.com/market-data/browse-data.html) · [DataMine historical source](https://www.cmegroup.com/datamine.html) · [real-time market data](https://www.cmegroup.com/market-data.html) · [data terms](https://www.cmegroup.com/trading/market-data-explanation-disclaimer.html).
- **Fields/data:** Product-specific packages may provide trade, quote, market depth/order-book, settlement, daily bulletin, and instrument/reference data for CME, CBOT, NYMEX and COMEX contracts. Exact message fields, depth, granularity, dates and symbols depend on chosen product/feed; obtain schema/sample and contract coverage before purchase. Exchange page advertises 40+ years history overall, not necessarily every product/field.
- **Access/timing/terms:** Historical downloads through DataMine are paid/product-priced; real-time streams and cloud/analytics access are subscription/entitlement products. Exchange pages distinguish real-time from delayed and historical products; no universal free executable feed. Market-data agreements, display/non-display use, redistribution and derived-data terms apply. Timestamp semantics depend on product: validate exchange event time versus publication/receive time, timezone, sequence and end-of-day convention from technical docs.
- **Limitations:** Claims are exchange product descriptions, not independent completeness tests. Contract rolls, expiries, corrections, block/EFRP inclusion, settlement methodology, session breaks and schema changes require explicit handling. A continuous series is derived, not a listed contract's actual price path.
- **Assessment:** Grade 1 for product/access facts; reviewed 2026-10-18; novelty moderate given existing directory's CME pointer. Source type: exchange commercial product documentation.

### Nasdaq public quote pages / exchange data products — listed equities, ETFs and options

- **Direct verified URLs:** [U.S. market data products](https://www.nasdaq.com/products/data) · [public stock screener](https://www.nasdaq.com/market-activity/stocks/screener) · [Nasdaq options chain page](https://www.nasdaq.com/market-activity/quotes/option-chain).
- **Fields/data:** Public pages provide security screening/listing information and displayed quote/last/volume/summary fields depending on instrument/page. Product catalog separately sells real-time and historical feeds/data sets. ETF is an instrument category using the equity market-data ecosystem; do not assume every screen field is a full ETF NAV/creation-redemption dataset. Option-chain displayed fields are not a complete consolidated OPRA event archive.
- **Access/timing/terms:** Website is accessible without an API key; displayed prices may be delayed (confirm the delay label on the selected page/instrument). Historical exchange datasets and real-time feeds require product purchase/entitlement; product and use rights vary. Page snapshot/retrieval time is not exchange event time. For systematic intraday use, license a defined feed and retain exchange timestamps/sequence.
- **Limitations:** Screen/page coverage and refresh cadence are not a stable research API contract. Nasdaq venue data do not equal consolidated U.S. market unless expressly designated. Public display quotes cannot support fill assumptions; ETF market price differs from NAV/iNAV.
- **Assessment:** Grade 1 for official page/product descriptions; reviewed 2026-10-18; novelty moderate (clear distinction between public page and licensed tape). Source type: exchange public pages and commercial data-product documentation.

### OCC — listed U.S. options reference and volume/statistical data

- **Direct verified URLs:** [OCC market data and reports](https://www.theocc.com/market-data) · [OCC data products](https://www.theocc.com/market-data/market-data-reports).
- **Fields/data:** OCC publishes options volume/open-interest reports, daily market statistics, clearing/contract reference information and product-specific data offerings. Reports can identify underlying/product, calls/puts, volume/open interest and date/contract series attributes depending on report. This is useful for option universe and activity context; it is not automatically quote/trade tick history. Verify report field definitions and download schema on the specific page.
- **Access/timing/terms:** Public report pages/downloads for published summaries; granular historical/reference products may have product-specific access/fees/agreements. Not a live executable quote endpoint. Daily report date is a business/reference date; page publication/processing time should be recorded separately. OCC data terms and any downstream exchange/OPRA entitlements govern reuse.
- **Limitations:** Aggregated volume/OI omit price, NBBO, aggressor, quote state, and venue execution details. Open interest is clearing-derived and may not equal same-day trading. Contract adjustments and symbol lifecycle must be mapped; daily snapshots cannot be used as intraday execution data.
- **Assessment:** Grade 1 for official published report/product documentation; reviewed 2026-10-18; novelty high (dedicated clearing/reference source beyond Cboe venue stats). Source type: U.S. options clearing corporation primary data publisher.

## Crypto venue public market data (venue-specific executable observations)

### Kraken public REST and WebSocket

- **Direct verified URLs:** [REST OHLC endpoint](https://docs.kraken.com/api/docs/rest-api/get-ohlc-data) · [WebSocket v2 market data](https://docs.kraken.com/api/docs/websocket-v2/ticker) · [API overview](https://docs.kraken.com/api/).
- **Fields/data:** OHLC endpoint provides pair, interval, candle start timestamp and OHLCV plus VWAP/trade count as returned by schema; last response item is current/uncommitted candle. Public ticker provides best bid/ask and related 24-hour fields; public trades/order-book WebSocket channels provide venue events/depth (channel-specific schema).
- **Access/timing/terms:** Public endpoints generally require no key for public market data; private account/trade actions require credentials. REST is snapshot/polling; WebSocket is streaming, not an exchange-wide consolidated feed. OHLC endpoint is limited to 720 recent entries regardless of interval, so not adequate for arbitrary long history. Current terms, rate limits, geographical/market availability apply.
- **Timestamp semantics/limits:** Candle timestamp is interval start (check current schema); last candle may be incomplete. WebSocket event timestamps are venue-provided and should be retained alongside local receipt time. Single venue, pair-specific asset conventions, outages, listing changes, gaps, forks and market-specific liquidity; does not represent global crypto price or executable size beyond observed book.
- **Assessment:** Grade 5 for provider-documented behavior; reviewed 2026-10-18; novelty moderate (directory already links OHLC, this adds precise cap and stream distinction). Source type: commercial exchange API documentation.

### Coinbase Exchange public market data

- **Direct verified URLs:** [product candles](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproductcandles) · [Exchange public trades](https://docs.cdp.coinbase.com/exchange/reference/exchangerestapi_getproducttrades) · [WebSocket feed overview](https://docs.cdp.coinbase.com/exchange/websocket-feed/overview).
- **Fields/data:** Candle rows contain time, low, high, open, close and volume; supported granularities are product-specific and endpoint has bounded candle count per request. Public trades include trade ID, price, size, side and time; WebSocket channels include ticker, matches/trades and level2 book messages as documented.
- **Access/timing/terms:** Public market endpoints do not require an authenticated key; public WebSocket subscription is available. Historical REST candles are capped at 300 per request and may omit intervals with no ticks; paginate or use licensed historical products for deep coverage. Venue terms, rate limits, regional product availability and redistribution rights still apply.
- **Timestamp semantics/limits:** Trade time is venue event timestamp; preserve receipt time separately. Candle `time` denotes candle period boundary (Unix seconds, UTC in documented payload); never treat an unfinished interval as final. Coinbase Exchange is one venue and product namespace, not Coinbase-wide/consolidated crypto.
- **Assessment:** Grade 5 for provider docs; reviewed 2026-10-18; novelty moderate. Source type: commercial exchange API documentation.

## Point-in-time ingestion patterns

### Treasury API snapshot (reference series)

Example request: `https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates?filter=record_date:gte:2025-01-01&sort=record_date&format=json`. Save request URL/parameters, raw JSON, HTTP retrieval time in UTC, response headers, and dataset/schema metadata. Treat `record_date` as the observation date, not release time. For strict PIT, archive each scheduled pull as an observed vintage and do not backfill latest corrected values into prior decision dates unless a timestamped release vintage proves availability.

### ECB SDMX vintage-aware retrieval

Discover flow/key/DSD first; fetch the exact series with the documented REST route, e.g. `https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2025-01-01&endPeriod=2025-01-31&format=csvdata`. Persist the SDMX key, response attributes/status, HTTP retrieval time and metadata version. Join by ECB observation date only after establishing the source publication/revision rule; for decision-time backtests use captured releases/vintages, not today's revised history.

### Venue-event ingestion (crypto or licensed exchange feed)

Subscribe to a named product/channel and store every raw message with `venue_event_time`, `sequence_or_trade_id`, `local_received_at_utc`, symbol, channel, connection/session ID and payload. Detect sequence gaps/reconnects, preserve snapshots plus deltas, and rebuild books only under the venue's documented sequence rules. For candles, store interval start/end, completion status, and retrieval/receipt time; exclude unclosed bars from finalized-bar features. A polling OHLC endpoint is not evidence that the value was available at every point inside its interval.

## Links and scope boundary

See [[Financial data source directory]] for the broader catalog and [[Data provenance and point-in-time]] for provenance cards, vintage handling, identifiers and as-of joins. Market-folder links: [[Forex]] · [[Fixed Income]] · [[Equities]] · [[ETFs]] · [[Futures]] · [[Options]] · [[Crypto]]. This note is deliberately limited to public/reference data and documented commercial source pages; no provider's coverage, best execution, or alpha claim is independently certified here.

## Sources checked

Pages/endpoints verified in this review: Treasury Fiscal Data API response and Treasury interest-rate page; ECB API overview and FX reference-rate page; BIS bulk-download page/API docs; CFTC COT page and PRE; CME browse-data and DataMine pages; Nasdaq data catalog/screener/options chain; OCC market data/report pages; Kraken REST OHLC and API documentation; Coinbase candles/trades/WebSocket documentation. Existing parent-directory entries were checked for duplication. The former OCC historical URL `https://www.theocc.com/market-data/market-data-reports/series-and-trade-information` returned 404; use the current market-data/report landing pages above and confirm specific report paths before ingestion. A previous Coinbase candles path returned 404; the current exchange reference path is linked above. Product terms and schemas can change; re-check before acquisition.
