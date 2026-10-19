# Point-in-Time Feature Availability Contract

## Definition and example

A feature is eligible at decision time \(t\) only if that exact version was usable by then. If publication time is \(p\), receipt time \(r\), and processing latency \(\ell\), earliest availability is \(a=\max(p,r)+\ell\); require \(a\le t\). For example, an 08:30:00 decision cannot use a release received at 08:30:02 and processed three seconds later, regardless of reference month.

Record reference/event time, publication, receipt, feature-ready time, timezone, revision ID, transformation/version, fit window, missingness meaning, and eligibility rule. Rolling transforms must use prior observations; fit scaling/imputation within training folds.

## Failure modes

- Date-only joins move after-close releases into earlier decisions.
- Latest revised values replace first releases.
- Full-sample normalization leaks future distribution.
- Vendor backfill is treated as contemporaneous history.
- Ambiguous timestamps assume favorable availability.

## Falsifiable exercise

Using archived releases, compare a vintage-aware series with latest-snapshot features under a frozen model and chronological test. Repeat with next-session lag. If predictive value appears only in revised/latest data, the real-time feature claim fails.

## Graded sources

- **Grade 1, primary documentation:** FRED observations API supports real-time periods/vintage dates. [Official docs](https://fred.stlouisfed.org/docs/api/fred/series_observations.html). Verify vintage availability per series.
- **Grade 1, primary documentation:** SEC EDGAR API documentation. [Official docs](https://www.sec.gov/edgar/sec-api-documentation). Filing metadata do not establish local system receipt latency.
- **Grade 1, general methods:** Kaufman et al. (2020), “Leakage in Data Mining.” [DOI](https://doi.org/10.1145/3338511). General leakage guidance, not market-specific evidence.

Related: [[Feature engineering]] · [[Data vintage and real-time testing]] · [[Research workflow]]
