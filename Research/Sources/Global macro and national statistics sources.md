# Global Macro and National Statistics Sources

**Scope:** shortlist of official channels that extend the vault beyond U.S. series. Grades are claim-specific (1 strongest, 10 weakest), not a blanket rating of economic accuracy. **Reviewed 2026-10-18**; recency is page review date, while actual dataset update dates vary. **Novelty: medium** as a cross-region access map, low for each agency's own documentation. **Source type:** official intergovernmental and national statistical/central-bank dissemination documentation.

## International and regional aggregators

### IMF Data / SDMX

- **Data:** cross-country national accounts, prices, labor, fiscal, external-sector and monetary/financial datasets. WEO includes historical data and projections; CPI includes country series; COFER is an example with confidential country submissions and an aggregated global composition.
- **Access/formats:** IMF documents SDMX 2.1 and 3.0 APIs. API exploration is linked through the portal's Swagger page, which its documentation says requires a beta portal account; do not assume every dataset/query is anonymously accessible. SDMX is structured, metadata-bearing exchange; inspect the dataset-specific output options in the API spec.
- **Release/revisions:** dataset cadence is dataset-specific: WEO twice yearly (April/October); COFER quarterly survey; other datasets differ. IMF explicitly documents a COFER revision/definition change starting 2025Q3, with revisions back to 2000Q1. Preserve the release vintage and notes; no universal historical vintage guarantee established.
- **Rights/limits:** IMF copyright and usage terms apply; check dataset terms and attribution/reuse provisions before redistribution. API reference does not establish a general quota, so none is asserted.
- **Evidence:** **Grade 1** for IMF-stated dataset contents, access and release/change claims; **series-specific** for reporting coverage and statistical methods. **Limitations:** compilation and reporting lag, missing country-periods, estimates/projections, breaks/benchmark revisions; some aggregates are confidential or imputed. An official current value does not prove it was available historically.
- **Point-in-time test:** Choose one monthly CPI series and one WEO observation. Save the first response, dataset metadata, release date, query and checksum; re-query after the next release and diff old periods. For strict backtests, require dated archived release files or mark prior vintages unavailable—do not infer vintages from today's API response.
- **Verified links:** [IMF Data](https://data.imf.org/en/) · [IMF API overview](https://data.imf.org/en/Resource-Pages/IMF-API) · [WEO dataset](https://data.imf.org/en/datasets/IMF.RES:WEO) · [COFER dataset and revision note](https://data.imf.org/en/datasets/IMF.STA:COFER) · [IMF copyright/usage](https://www.imf.org/external/terms.htm)

### OECD SDMX

- **Data:** OECD member/partner-country statistics, including national accounts, prices, labor, trade, productivity, public finance and structural indicators; exact coverage depends on each dataflow.
- **Access/formats:** official SDMX API and public API documentation/Swagger; SDMX REST supports data and structural metadata queries. Use dataflow and DSD metadata to construct valid keys; format/media-type choices are API-version and endpoint-specific. Authentication requirements and any throttling should be checked against current docs for the intended operation; do not assume a quota.
- **Release/revisions:** frequency and schedule belong to each dataset and indicator. Current API data are not a substitute for dated publication vintages; capture release calendars/publication and revision notes per dataset.
- **Rights/limits:** OECD reuse and licensing terms vary by material; check dataset-specific terms and attribution, especially redistribution/commercial use. No general quota claimed.
- **Evidence:** **Grade 1** for OECD API/dataflow documentation; **series-specific** for observation comparability. **Limitations:** national source differences, harmonization, missingness, breaks and revisions; common labels do not imply identical definitions or release times.
- **Point-in-time test:** discover a dataflow, save its DSD and a small monthly/quarterly query, then repeat after a scheduled release. Compare observations, flags and structure. Verify whether dated historical releases are retrievable before using current history in an as-of backtest.
- **Verified links:** [OECD SDMX API portal](https://sdmx.oecd.org/public/swagger/index.html) · [OECD Data Explorer](https://data-explorer.oecd.org/) · [OECD data terms](https://www.oecd.org/en/about/terms-conditions.html)

### Eurostat API

- **Data:** harmonized EU/EEA national accounts, HICP, labor, prices, trade, government finance, population and other social/economic datasets.
- **Access/formats:** public REST services, no API key described as necessary; official documentation lists SDMX-ML, SDMX-CSV, JSON-stat and TSV, with SDMX 2.1/3.0, statistics and catalogue interfaces. Endpoint and output-format support vary by API.
- **Release/revisions:** Eurostat says database updates run twice daily at 11:00 and 23:00 CET when newer data or structural changes exist. It explicitly says the online database contains latest versions and does not provide versioning/documentation of past versions. Eurostat release calendar and dataset metadata provide release context, not a general vintage archive.
- **Rights/limits:** free API access; Eurostat permits commercial/non-commercial reuse with acknowledgment, but dataset-specific and third-party exceptions apply (including some non-EU data). Check the copyright notice for the exact series. No universal request quota claimed.
- **Evidence:** **Grade 1** for API formats, update cycle and latest-version-only caveat from current official guide. **Limitations:** current revised series can overwrite information; revisions and benchmark rebasing, national reporting lags, flags and dataset structure changes must be tracked.
- **Point-in-time test:** query a named dataset and save JSON-stat/SDMX response plus `last update`/metadata and receipt timestamp; repeat after a known release and compare. Since past versions are not documented in the database, archival snapshots are required for strict vintage testing.
- **Verified links:** [API introduction](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction) · [API getting started](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-getting-started) · [Data revision policy](https://ec.europa.eu/eurostat/en/data/data-revision-policy) · [Reuse notice](https://ec.europa.eu/eurostat/en/help/copyright-notice)

### UNData SDMX

- **Data:** UN and partner-agency datamarts, including national accounts, population, trade, energy and environment; actual datasets and country coverage are datamart-specific.
- **Access/formats:** REST and SOAP SDMX services; REST documentation supports XML, JSON and CSV (CSV data only). Browse dataflows and DSDs before building queries. Public docs describe service use without an API key; no general quota is published in the reviewed docs.
- **Release/revisions:** UNData's update calendar exists, but source series have individual schedules. UNData states it may incorporate revisions/updates without notice and does not guarantee timeliness. Latest-state retrieval is not a historical vintage service.
- **Rights/limits:** UNData terms say data/metadata may be copied and redistributed if UNData is cited; underlying source provenance and third-party restrictions still matter. Terms disclaim guarantees of accuracy/timeliness/completeness.
- **Evidence:** **Grade 1** for API and stated terms; **Grade 2** for aggregate update/revision behavior because underlying publishers control source series. **Limitations:** API coverage is incomplete where datamarts lack DSD mappings; data are supplied as present in source databases, not necessarily harmonized or real-time.
- **Point-in-time test:** query dataflow and DSD, capture one filtered series in CSV and XML/JSON with metadata and date; compare against the cited source agency's release. Re-query after its next update and test whether old values changed. Preserve dated snapshots for as-of work.
- **Verified links:** [API manual](https://data.un.org/Host.aspx?Content=API) · [REST dataflow discovery](https://data.un.org/ws/rest/dataflow/) · [UNData terms](https://data.un.org/Host.aspx?Content=UNdataUse) · [Update calendar](https://data.un.org/UpdateCalendar.aspx)

## National sources: Asia and Latin America

### Reserve Bank of India (RBI)

- **Data:** Indian monetary/banking, rates, FX/reserves, payments, CPI/WPI, industrial production, trade, balance of payments, debt and survey releases. RBI's release index explicitly groups releases by daily through annual cadence; monthly Bulletin tables link XLSX and PDF, and DBIE is the time-series database.
- **Access/formats:** web tables, spreadsheet/PDF downloads and DBIE portal. Reviewed documentation did not verify a stable public API or a universal authentication rule; use the published portal/download interface and check access at acquisition. No quota claimed.
- **Release/revisions:** release timing varies by series; RBI links an SDDS advance-release calendar and lists weekly/monthly/quarterly schedules. Bulletin issue has a dated publication page. Revisions and historical series behavior are not uniform; preserve dated files and release notices.
- **Rights/limits:** RBI site disclaimer/terms govern reuse; verify specific document/data permissions and attribution before republication. Do not infer redistribution permission from spreadsheet availability.
- **Evidence:** **Grade 1** for official release catalogue, listed frequency categories and actual dated Bulletin attachments; **series-specific** for first-publication time and revisions. **Limitations:** mixed frequency, dissemination via documents, series/base-year changes and revised or provisional values; many monthly tables are not released at the beginning of their reference month.
- **Point-in-time test:** select a named CPI or FX/reserve table; save the dated Bulletin XLSX/PDF, publication page, release-calendar entry and receipt time. Compare successive issues for historical revisions/schema changes, and only expose data to a backtest after documented publication time.
- **Verified links:** [RBI Data Releases](https://www.rbi.org.in/Scripts/Statistics.aspx) · [RBI Bulletin archive](https://www.rbi.org.in/Scripts/BS_ViewBulletin.aspx) · [Database on Indian Economy](https://data.rbi.org.in) · [SDDS advance release calendar](https://www.rbi.org.in/Scripts/SDDSview.aspx)

### INEGI (Mexico) Indicator Bank API

- **Data:** Mexican national, state and municipal indicators, subject to geography available for each indicator; includes CPI, activity and other official measures. Responses include frequency, unit, notes, status, source, last-update date and observation periods/values.
- **Access/formats:** API v2.0 documentation says a registered token is required. Supports JSON, JSONP and XML; PC-Axis and JSON-stat options are also documented. Query may request latest observation or full history.
- **Release/revisions:** documentation reports indicator periodicity and `LASTUPDATE`, but the API page does not promise a fixed common release calendar or preserve old versions. Consult each indicator's source and release calendar; capture responses on receipt.
- **Rights/limits:** INEGI's terms permit copying, publication, adaptation and commercial use subject to preserving metadata, attribution, noting transformations and not implying agency endorsement. Check current terms; token required. No request quota stated.
- **Evidence:** **Grade 1** for documented API parameters, token, output formats and response fields; **series-specific** for definitions and revisions. **Limitations:** indicator IDs/geographic availability vary; heterogeneous originating programs, stale or revised observations, and returned current history do not establish historical availability.
- **Point-in-time test:** obtain a token; query the same indicator once with full history and once for latest only; save raw response, `LASTUPDATE`, observation status and receipt timestamp. Repeat after its documented update and diff both values and metadata; locate an archived release before treating history as point-in-time.
- **Verified links:** [INEGI API developer guide](https://www.inegi.org.mx/servicios/api_indicadores.html) · [Indicator API example endpoint pattern](https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000001/es/00/false/BISE/2.0/TOKEN?type=json) · [INEGI terms and free-use conditions](https://www.inegi.org.mx/inegi/terminos.html)

## Practical selection

For broad comparability begin with IMF/OECD/Eurostat, then use national publishers to verify definition, local release timing and revisions. UNData is a useful discovery/aggregation layer, not a replacement for a source agency when release-vintage integrity matters. For every series record reference period, first publication timestamp/timezone, receipt timestamp, revision/vintage status, unit/base, seasonal adjustment, flags, source geography and terms in [[Data provenance and point-in-time]]. A source's official status supports the claim about what it published; it does not establish predictive utility.

## URLs checked

Official pages successfully reviewed: IMF Data home and API overview; IMF WEO and COFER dataset pages; OECD SDMX Swagger portal and Data Explorer; Eurostat API introduction and getting-started documentation; UNData API manual, terms and update calendar; RBI Data Releases, Bulletin archive and DBIE; INEGI API developer guide. IMF main-site `/en/Data` returned 403 in the fetcher, while `data.imf.org` pages were accessible; OECD explainer candidate returned 404, so relied on the official Swagger portal. The direct OECD sample data request was blocked by the fetcher (403), so endpoint behavior beyond official portal documentation is not asserted. Reviewed terms links are included above; confirm current terms before use.

## Related notes

[[Financial data source directory]] · [[Data provenance and point-in-time]] · [[Data dictionary and provenance card]] · [[Data vintage and real-time testing]]
