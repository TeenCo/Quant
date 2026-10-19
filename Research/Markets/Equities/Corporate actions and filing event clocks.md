# Corporate actions and filing event clocks

Parent: [[Equities]]. Related: [[ETFs]], [[Financial data source directory]].

## Event timestamps and return arithmetic

Separate event announcement, ex/effective date, record date, payable date, filing acceptance/public dissemination, vendor ingestion, and strategy decision time. For a cash dividend D, idealized ex-date price drops by D, while total return adds the distribution: \((P_1-P_0+D)/P_0\), with reinvestment convention stated. A split ratio k new shares per old share transforms shares \(q'=kq\), price \(P'=P/k\); value is invariant absent market movement. Spin-offs, rights, mergers, and special distributions need event-specific terms.

## Example

A $50 stock pays a $1 cash dividend and closes ex-date at $49.20. Price return is -1.6%; simple total return is \((49.20-50+1)/50=0.4\%\). Labeling price-only return as investor loss omits the cash distribution. If announced after close, that announcement cannot explain the earlier close.

## Fields and clock

Keep stable issuer/security identifiers, filing accession, acceptance and dissemination timestamps/time zone, form, amendment linkage, fiscal period, XBRL concept/unit/context, raw and adjusted prices, action type/ratio/cash, announcement/ex/record/pay dates, source publication and ingestion times, exchange calendar, halt/auction state and point-in-time universe membership. EDGAR acceptance is a public-availability proxy; verify dissemination timestamp and after-hours session handling.

## Failure modes

Back-adjust with future action knowledge; use fiscal period end as release time; overwrite original filings with amendments; confuse split-adjusted units and EPS; omit delistings/merger consideration; treat vendor corporate-action date as announcement; mix local and UTC timestamps; assume every distribution is ordinary cash dividend.

## Falsifiable exercise

Choose a filing form and surprise definition before sampling. Build event windows from acceptance timestamp plus a fixed processing delay, separate regular/after-hours releases, and compare executable returns to matched non-event sessions. Re-run using first dissemination versus acceptance and exclude confounded events under predeclared rules. Report sensitivity; no causal or alpha claim without identification and costs.

## Source leads

- SEC EDGAR APIs (primary official data; grade 1 for submission metadata, live docs, high operational value; API access/rate limits apply and acceptance time is not an execution guarantee): https://www.sec.gov/search-filings/edgar-application-programming-interfaces .
- SEC XBRL API documentation (primary technical docs; grade 1 for endpoints, current; facts can be amended/restated and unit/context interpretation remains necessary): https://www.sec.gov/edgar/sec-api-documentation .
- Nasdaq corporate actions (exchange source; grade 3 for its listed notices, current service; not a complete cross-market history): https://www.nasdaq.com/market-activity/corporate-actions .
