# LSE Catalog Coverage Review — 2026-10-18

This note summarizes a user-authorized, local metadata-only catalog snapshot. It contains aggregate coverage counts, not the row-level catalog or historical market observations. The original JSON/CSV and analyzer outputs remain in the user's local `lse_catalog_snapshot` folder and should stay private under the provider's terms.

## Snapshot provenance

- **Source:** London Strategic Edge Python SDK `catalog()` response.
- **SDK version:** 0.14.0.
- **Retrieved:** initial snapshot 2026-10-18T13:07:53Z; refreshed snapshot 2026-10-18T13:51:38Z.
- **Catalog rows:** 22,966.
- **Unique `(dataset, symbol)` keys:** 22,966; no duplicate pairs observed.
- **Catalog-reported tick-count sum:** 137,473,395,316. This is provider metadata, not rows acquired, a guarantee of exportability, or a cross-dataset comparable count.
- **Files:** raw catalog JSON/CSV plus generated `analysis/lse_catalog_coverage_report.md` and `analysis/lse_catalog_enriched.csv`, all local and outside the Obsidian vault.
- **Scope:** metadata only; no historic bars, ticks, options prints, reference tables, or live stream was requested.

A second authorized catalog request at 13:51:38Z returned the same 22,966 keys and no changes in `first`, `last`, `ticks`, `country`, or `name` compared with the initial snapshot. This documents agreement between these two snapshots only; it is not proof of complete or stable source history.

## Catalog count by category

| Provider category | Entries | Earliest `first` shown | Latest `last` shown | Interpretation/caveat |
|---|---:|---|---|---|
| Economics | 14,911 | 1900-01-01 | 2027-03-01 | Largest category. Catalog has 208 country labels. 29 entries have `last` later than the snapshot date; inspect for forecasts, scheduled effective dates, or metadata issues before treating them as observations. |
| Stocks | 3,982 | 2003-09-10 | 2026-10-17 | Country labels cover 53 distinct values, with 77 missing. Catalog alone does not establish survivorship-free history or corporate-action correctness. |
| Options | 3,186 | 2014-06-02 | 2026-10-16 | 40 country labels; records may represent underlying/contract coverage differently. Verify whether entries are underlyings, contracts, prints, bars, or a mixture per endpoint. |
| Forex | 62 | 2009-09-25 | 2026-10-16 | Catalog country field is blank; venue/feed and global-volume meaning require verification. |
| Crypto | 58 | 2017-08-17 | 2026-10-18 | Catalog country field is blank; venue, pair and market segmentation require verification. |
| Futures | 68 | 2025-03-11 | 2026-10-16 | History begins comparatively recently in this snapshot; contract-level versus continuous identifiers and expiry lifecycle need inspection. |
| ETFs | 25 | 2026-04-27 | 2026-10-16 | Short catalog history span in this snapshot; check whether the catalog describes only a new dataset version or actual history limitation. |
| Bonds | 202 | 1990-01-01 | 2026-09-10 | 34 country labels. Determine whether values are evaluated yields, quotes, or other series before use. |
| Corporate bonds | 192 | 2020-01-01 | 2026-10-12 | 32 country labels; issuer/issue identity, liquidity, and evaluated-price semantics need validation. |
| Sovereign yields | 88 | 2010-01-01 | 2026-10-12 | 9 country labels; reference series are not executable bond quotes. |
| Credit indices | 79 | 2010-01-04 | 2026-10-12 | 4 country labels; index definitions and currency/constituent vintages require inspection. |
| FX derivatives | 63 | 2015-01-01 | 2026-10-12 | 5 country labels; confirm product type, contract identity, and whether observation is price, settlement, or reference. |
| Commodities | 23 | 2026-04-27 | 2026-10-16 | Short catalog range relative to conventional futures history; verify whether this is a distinct spot/CFD dataset or limited product history. |
| Indices | 19 | 2023-02-14 | 2026-10-16 | Confirm index calculation, level/return, constituent vintage and update times. |
| Interest rates | 4 | 2026-06-30 | 2026-10-16 | Recent-looking coverage in this snapshot; compare with official historical benchmarks before selecting. |
| Bond futures | 2 | 2010-01-04 | 2026-10-12 | Only two catalog entries; check underlying contracts and history before assuming broad coverage. |
| Volatility | 1 | 2026-07-01 | 2026-10-07 | Single entry with short range; identify metric/product and compare with official index source. |
| Currency index | 1 | 2026-06-30 | 2026-10-07 | Single entry with short range; establish construction and historical coverage. |

## Metadata QC

- All 22,966 records have a symbol, name, category, dataset, tick-count field, first, and last values in this snapshot.
- Country is blank for 241 records, concentrated in instrument classes where a country field may not apply; this must not be imputed from a symbol without a separately validated mapping.
- No duplicate `(dataset, symbol)` keys, missing/blank first/last/tick fields, reversed date intervals, or negative tick counts were detected.
- 29 economic series have a catalog `last` date after snapshot date (maximum 2027-03-01). That is a review flag; it may reflect projections, known effective dates, or a provider metadata issue. It is not evidence of future observations actually received.
- Dates in the catalog are not accompanied here by a documented timezone, event/publication semantics, or revision/vintage behavior. Timestamp parsing must preserve the original value; do not silently label naive values UTC.

## Authorized vault preflight — 2026-10-18T13:55:55Z

The user's local metadata-only preflight succeeded with SDK 0.14.0 and made no historical-data or live-tick requests.

- Vault metadata lists 18 dataset classes; 7 candle classes (`commodity`, `crypto`, `etf`, `futures`, `fx`, `index`, `stocks`), plus 3 synthetic candle classes (`currency_index`, `interest_rates`, `volatility`); 14 general candle timeframes from 1s to 1mo.
- Series classes: `bond_futures`, `bonds`, `corporate_bonds`, `credit_indices`, `economics`, `fx_derivatives`, `sovereign_yields`. The metadata explicitly lists `bonds` series resolutions as 1d/1h.
- Options metadata lists chain, flow, and 1m-flow, with 10 option candle timeframes from 1m to 1mo.
- Reference inventory reports 12 datasets: options_flow 344,445,053 rows; options_flow_1m 308,714,730; insider_trades 14,913,089; financial_reports 2,459,808; options_chain 2,317,078; dividends 929,282; bond_yields 716,820; economic_calendar 147,193; stock_splits 46,823; COT 34,608; company_profiles 8,304; stock_fundamentals 8,304. These are provider-side inventory counts, **not downloaded rows**.
- Account usage at that timestamp: 0 bytes used of 53,687,091,200 monthly and 16,106,127,360 weekly caps; 0/5 export jobs used this hour; 200 API calls/minute; 5,000 max rows/request; concurrency 2. `historical_data_months=-1` is retained as the raw returned value; its meaning is not inferred.
- These limits and counts are a timestamped snapshot, not guaranteed quota or exportability for each dataset. Verify before acquisitions. Five export jobs/hour plus byte caps mean full-catalog exports should be planned and staggered.

## Bounded sample results — 2026-10-18T14:01:51Z

The user-approved sampler made 29 non-export calls (maximum 3 rows per call), all successful. The local artifact was transformed into 80 normalized sample rows with a manifest; outputs remain private outside the vault. Ten candle/synthetic classes returned a shared OHLC shape, seven series classes returned `(date, symbol, value)`, and reference/options methods had distinct schemas. All 36 sampled OHLC bars passed basic range checks.

One critical anomaly: `options(underlying="SPY", max_dte=30, limit=3)` returned July 2, 2026 contracts with `updated_at` in June/July, while the sample was retrieved October 18; reported DTEs were stale relative to retrieval time. These samples were expired at retrieval and demonstrate that method success does not imply freshness. See [[LSE bounded schema sample findings 2026-10-18]]. Block chain-based research until the endpoint semantics are clarified and freshness is verified.

## Full acquisition feasibility

The preflight reveals the scale and limits that should govern any interpretation of “exhaust the available dataset”:

- There are 4,243 catalog entries in candle/synthetic-candle classes (stocks, FX, crypto, ETFs, futures, commodities, indices, currency indices, interest rates, volatility). One `history()` Parquet export per entry at a single resolution would mean at least 4,243 export jobs. At the stated maximum of 5 jobs/hour, that is a theoretical lower bound of **849 export-job hours** (about 35.4 continuous days), before retries or data-size limits.
- Exporting all 14 candle resolutions for those entries would require up to 59,402 jobs; including raw tick tape as another resolution could raise this to roughly 63,645 jobs—about 12,729 export-job hours (530.4 continuous days) at the stated cap. This is a scale illustration; the provider may bundle, reject, or differently count some requests.
- The account also reported byte caps of 15 GiB/week and 50 GiB/month, concurrency 2, and large reference inventory row counts. Catalog `ticks` are not file-size estimates, so storage and throughput cannot be predicted before a small export-size study.
- Export jobs may be limited to five/hour independently of read calls. `history()` is an export path; synchronous bounded candles/series/reference calls are separate and capped at 5,000 rows/request per preflight metadata.

Thus exhaustive treatment should be **complete accounting and disposition of all catalog entries**, then exhaustive acquisition of a user-approved, licensed research subset by family/timeframe. Downloading every raw tick, all 14 candle resolutions, all options, and all reference tables is not a single pass and cannot responsibly be inferred from the present catalog/limits.

## Coverage implications

The snapshot has **breadth of listings**, but demonstrated historical depth is uneven. Economics dominates row count; market-history categories vary substantially in dates, and some—ETFs, commodities, interest rates, volatility and currency index—show short ranges. Underlying provider tick totals are heavily concentrated in stocks, FX and crypto and cannot be treated as comparable observations across datasets.

The catalog reports 22,966 dataset-symbol entries; the schema does not prove that every dataflow, frequency, contract, time span, or field can be exported. The next “exhaustive” task should therefore mean inventorying and dispositioning every listing, then exhaustively exporting **only a defined and licensed subset**. An indiscriminate full-history pull is not justified by this catalog: it could be quota/cost intensive, duplicate data, include unsuitable revised histories, or exceed storage and permission boundaries.

## Staged acquisition decision

1. **Catalog reconciliation (done):** preserve snapshot, categorize all rows, inspect duplicates/missingness/date anomalies.
2. **Rights and schema registry:** for each dataset family, capture terms, fields/units, clock, native resolution, revisions, export availability, and quota. Unknown fields remain explicit.
3. **Representative sample, one per family:** request a small bounded slice only after the provider's current API docs/terms are verified; validate independent values and returned schemas.
4. **Tier acquisition:** prioritize user-selected research-relevant sources. Divide by instrument and bounded time interval, write partitions atomically, and reconcile every requested partition as complete/partial/restricted/unavailable/failed.
5. **Transform:** preserve provider data locally under applicable terms; create canonical and point-in-time layers with lineage and QC reports. Do not put raw provider records into the vault or a shared repository.
6. **Coverage close-out:** enumerate all catalog rows with a documented status, including those deliberately not exported and why. “Exhausted” means every row has a disposition, not indiscriminate data copying.

## Selected daily/series + reference acquisition manifests

The user selected all cataloged daily candles and all series, with reference tables staged separately. The local resumable daily/series manifest contains **19,780 tasks**: 4,243 1d candle symbols and 15,537 series symbols. It pages at at most 5,000 rows/request and writes private JSONL partitions with a SQLite status/continuation manifest. At 200 calls/minute, 19,780 one-page requests would have a theoretical floor of about 99 minutes; 0.4-second pacing gives a floor around 132 minutes, plus network latency and additional pages.

The reference-export manifest contains **692 date partitions**: 401 daily, 5 monthly, 284 yearly, and 2 snapshot tasks across the 12 reference datasets. At five exports/hour, this is a theoretical lower bound of 138.4 job-hours (about 5.8 continuous days), before byte caps, failures, and quota resets. Options flow/1m account for most daily partitions and contain very large provider inventory counts; actual Parquet sizes are unknown. The queue starts with the smallest row-count estimates, and the first execution should be one job to learn actual file size.

These are work-estimate lower bounds, not a commitment to run every task. The selected scope excludes raw-tick and every sub-daily resolution unless later specifically added. The reference queue is date-partitioned, with product-specific boundary semantics still needing validation; duplicate/omission checks are part of reconciliation.

Use [[Exhaustive dataset inventory and transformation protocol]], [[Tools/Inventory LSE catalog]], [[Tools/build_lse_sample_plan.py]], [[Tools/Sample LSE endpoint schemas]], [[Tools/Run LSE daily series sync]], and [[Tools/Plan and run LSE reference exports]]. Both runners have preview modes and local resumable manifests. Do not start either acquisition until the user reviews the plan, rights, storage, and quota reserves.

## Related notes

[[Financial data source directory]] · [[Data provenance and point-in-time]] · [[London Strategic Edge]] · [[Data validation patterns]] · [[Research pipeline architecture]] · [[Source grading]]
