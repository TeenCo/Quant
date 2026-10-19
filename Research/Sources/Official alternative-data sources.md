# Official and Vendor Alternative-Data Source Notes

This source note distinguishes a data publisher's documented product from a claim that the data is complete or predictive.

- **Evidence grade:** 1 for official agency documentation of published data/access semantics; 5 for commercial AIS vendors' own coverage/product claims. Grades apply to claim type, not the whole page.
- **Recency:** Pages reviewed 2026-10-18; verify limits, schedules, schemas, and terms before acquisition.
- **Novelty:** Low for official source documentation; medium as a cross-source map for physical-market research.
- **Source type:** Government primary documentation and commercial-vendor product documentation.

## EIA Open Data

- **Type:** U.S. government statistical agency, energy API and bulk downloads.
- **Docs:** [Open Data](https://www.eia.gov/opendata/) · [Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/)
- **Grade:** 1 for agency documentation and issued observations; series-level methods/latency still vary.
- **Useful:** Weekly inventory/balance and import/export tables, natural gas storage, power load/generation, prices, outages, projections.
- **Access:** API registration/key; terms and reuse policy linked by EIA. Bulk files are listed and EIA documents a twice-daily update process.
- **Caveats:** Survey estimates, preliminary/final status, changing report tables, rounding, revision and release schedule. Keep release vintage; distinguish projection from realized data.

## NOAA NCEI Climate Data Online

- **Type:** U.S. government climate archive and web-service API.
- **Docs:** [CDO Web Services v2](https://www.ncei.noaa.gov/cdo-web/webservices/v2)
- **Grade:** 1 for service descriptions and published station observations.
- **Access:** API token; official docs state 5 requests/second and 10,000 requests/day per token. Data endpoint has date-span and pagination limits.
- **Caveats:** Station relocation, equipment changes, reporting latency, missingness, quality flags, aggregation/unit choices, and data revisions. Model local weather/exposure, not just nearest-station readings.

## U.S. Census International Trade API

- **Type:** U.S. government trade statistics.
- **Docs:** [International Trade datasets](https://www.census.gov/data/developers/data-sets/international-trade.html)
- **Grade:** 1 for published data and methodological descriptions.
- **Timing/versioning:** Monthly series from January 2010 to present, updated on release day; Census says previously released monthly trade data are revised annually with April statistics.
- **Access:** API key now required per page; endpoints permit product/country/district/state/port classification queries.
- **Caveats:** Monthly publication lag, annual revision, classification changes, confidentiality suppression, valuation and quantity definitions. Release date is the information time; reference month is not.

## EIA Weekly Petroleum Status Report (WPSR)

- **Type:** EIA weekly energy market report with CSV/XLS/PDF tables and archives.
- **Docs:** [WPSR](https://www.eia.gov/petroleum/supply/weekly/)
- **Grade:** 1 for EIA's own report and methodology.
- **Useful tables:** Petroleum balance, refinery inputs/production, stocks, imports/exports, preliminary crude imports, and estimates.
- **Caveats:** Release clock and holiday shifts; totals may not exactly sum due to independent rounding. EIA posts notices when tables are discontinued or changed; report pages also include errata and methodology. Avoid scraping a current table as if its structure was constant.

## MarineTraffic / Kpler maritime intelligence

- **Type:** Commercial maritime AIS and event/derived-data product.
- **Docs:** [MarineTraffic Data Services](https://www.marinetraffic.com/en/ais-api-services) · [Kpler developer portal](https://developers.kpler.com/)
- **Grade:** 5 for provider's own coverage and service claims; independently test empirical completeness.
- **Advertised product areas:** Real-time AIS, historical tracks (page claims archive since 2010), vessel database, port/operational events, and predictive ETA/destination products.
- **Access:** Commercial service / request-demo path; developer documentation and terms govern use. No open unlimited full-history download established by reviewed page.
- **Caveats:** Terrestrial/satellite reception coverage, transmission gaps, identity resolution, AIS spoofing/manipulation, inferred cargo/destination, backfills, model-generated event labels, and changing receiver network. Retrospective predictions may not equal the forecast that existed at the time.

## Source-use principle

For each source, keep provider documentation as a primary source about product behavior and a lower-grade source about completeness or alpha. Preserve raw inputs, query/version, release/receipt time, terms, and separate model-derived fields from direct measurements.

## Related notes

[[Financial data source directory]] · [[Data provenance and point-in-time]] · [[Alternative data opportunity map]] · [[Alternative-data research design]]
