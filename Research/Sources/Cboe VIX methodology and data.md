# Cboe VIX Methodology and Data

## Bibliography

- **Authors / organization:** Cboe Global Markets
- **Date / version:** Web pages reviewed 2026-10-18; pages may change. Historical CSV is updated daily according to the historical-data page.
- **Publication / source type:** Exchange methodology/product and data documentation; primary source for Cboe index and product descriptions.
- **Source type:** Official exchange methodology, contract/product, and historical-data documentation.
- **DOI / stable identifier:** Not applicable.
- **Primary links:** [VIX overview](https://www.cboe.com/tradable-products/vix/); [VIX historical data](https://www.cboe.com/tradable-products/vix/vix-historical-data); [VIX term structure](https://www.cboe.com/tradable-products/vix/term-structure/); [VIX FAQ](https://www.cboe.com/tradable-products/vix/faqs/); [VIX options specifications](https://www.cboe.com/tradable-products/vix/vix-options/specifications/)
- **Open full text / permitted local file:** Public web documentation and CSV link; no local copy retained.

## Assessment

- **Evidence grade (1 strongest–10 weakest):** **2** for Cboe product/methodology and data-description claims; **5** for performance/strategy implications because exchange educational pages are not independent evidence of net strategy returns.
- **Recency / current applicability:** Current official pages inspected on 2026-10-18. Confirm page details and contract specs at the time of each study.
- **Novelty:** Low for methodology; high practical value for connecting official index, contracts, and historical data.
- **Claim(s) evaluated:** VIX is an SPX-option-derived constant-maturity implied-volatility index; Cboe provides daily historical VIX index values and a term-structure interface; the index and volatility derivatives are distinct products.
- **Methods / data:** Cboe describes the index as based on SPX option quotes and a constant 30-day horizon; historical index page links daily OHLC CSV beginning in 1990 and legacy VXO data; term-structure page describes point-in-time lookup and approximately 15-second intraday updates.
- **Main findings:** Official descriptions distinguish index values, VIX futures, and VIX options. The historical page's CSV fields are DATE, OPEN, HIGH, LOW, CLOSE. The page warns that data are provided for convenience and accuracy is not guaranteed. Term-structure page similarly disclaims accuracy and notes limited availability periods.
- **Limitations / caveats:** Cboe is authoritative about its own index and products but is also the exchange/operator. Daily VIX values do not reproduce option surfaces, establish point-in-time availability for an intended timestamp, or provide executable returns. Product marketing claims such as hedging or risk-premium strategies require independent testing. Data licensing/redistribution is product-specific; check current terms.
- **Replication / follow-up:** Use detailed methodology and contract-specific historical data for index reconstruction or derivatives research. Compare option-implied forecasts to matched realized variance with chronological, dependence-aware methods; evaluate trading only with executable quotes, hedging, roll, margin, and costs.

## Research use

- **Implication for quantitative finance:** An official index series is a useful explanatory or forecast input, but is not a tradable proxy for its derivatives. Track index methodology, contract settlement, timestamp, and data availability separately.
- **Potential experiment / falsification:** Test whether a pre-defined SPX option-implied variance measure improves out-of-sample realized-variance forecasts over historical/EWMA baselines; test strategy P&L separately with historical contracts and conservative execution assumptions.
- **Related notes:** [[Markets/Options/Implied volatility, variance risk premium and VIX]] · [[Markets/Options/Options]] · [[Econometrics/Volatility models]] · [[Econometrics/Forecast evaluation]] · [[Data provenance and point-in-time]] · [[Execution costs and market impact]]
- **Copyright/access note:** Links and summaries only. Cboe raw data terms and content permissions must be checked for each intended use; no data or PDFs copied locally.
