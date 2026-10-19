# London Strategic Edge: Data Access and Dependencies Walkthrough

> **Checked:** 2026-10-18. Website and SDK capabilities/limits can change; verify the current API documentation and account usage before relying on them.

London Strategic Edge (LSE) presents itself as a free market-data archive and research platform. Its website advertises historical data downloads, REST access, live WebSocket access, charts, backtesting, and an ML Studio. The public Python SDK provides a practical programmatic entry point for market-history queries and live streaming.

## What is needed?

### Option A — Web platform

Use the free-dataset portal, charts, backtesting, and ML Studio via a browser. The pages are JavaScript-driven. Platform processing is browser/service-based; the accessed pages do not disclose the full underlying model runtime environment. No local Python package is necessary for this option.

### Option B — Python data SDK (recommended for repeatable local research)

1. **Python 3.8+** (SDK metadata lists Python `>=3.8`; a current supported version is preferable).
2. A free LSE API key, available through the LSE data page/account flow.
3. Install `lse-data` from PyPI.
4. Base dependency: `websockets>=11.0` (for the client package/live socket support).
5. Optional DataFrame workflow: install the `frames` extra, which adds `pyarrow>=14` and `pandas>=1.5` for convenient DataFrame-returning bulk history/dataset calls. Without it, bulk export returns/downloads Parquet files rather than a DataFrame.
6. Network access to LSE's HTTPS API and WSS data endpoint. REST calls require the API key; the SDK accepts a key argument or `LSE_API_KEY` environment variable.

The SDK repository identifies itself as MIT-licensed, but that license covers the **client library only**, not the data. Its README points to the provider's terms, which prohibit redistributing/reselling LSE data or making it available to third parties. Review current terms and the specific source-data rights before retaining or using any dataset.

The current public README also says provider data may be used for the account holder's own research, trading, and model training (including commercial use), while prohibiting redistribution, resale, or making the data available to third parties. Treat this as a provider statement and confirm the current signed terms and any product-specific conditions before building a workflow.

## Setup

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install "lse-data[frames]"
```

For Parquet-file-only bulk use, install the base package instead:

```powershell
python -m pip install lse-data
```

Set the key in the current PowerShell session (avoid writing it into a notebook, source file, or shared vault):

```powershell
$env:LSE_API_KEY = "your_key_here"
```

The SDK also accepts `LSE(api_key="...")`. Prefer environment variables or a secrets manager for local scripts; never commit the key.

## Step-by-step: obtain and inspect one dataset

1. **Obtain an API key** through the official [LSE data portal](https://londonstrategicedge.com/data). Confirm account status and current quota in the portal/API.
2. **Find the exact instrument and source span** using `client.catalog("forex")`, `client.catalog("crypto")`, `client.catalog("stocks")`, or a relevant category. Inspect symbol, dataset, first/last observation, and coverage before forming a hypothesis.
3. **Start with a small, explicit time slice** using `candles(symbol, timeframe, start, end)`; the SDK documents 14 resolutions from 1-second to monthly bars. Note that its sync REST query method caps a response at 5,000 rows per call and supports date filtering/paging.
4. **For bulk history**, use `history()` or `dataset()`; the README says these run Parquet export jobs and count against an export-job budget. Space requests out and inspect `GET /vault/usage` or the account's equivalent to verify current quota.
5. **Check schema and semantics locally:** inspect column names, timestamp zone/convention, row count, duplicate timestamps, gaps, OHLC validity, sample values, and start/end dates. Compare a sample to an independent source where practical.
6. **Store a provenance record** alongside the experiment: retrieval time, exact symbol/dataset, date range, query parameters, package version, schema, data terms, and any transformations. Keep raw files immutable.
7. **Only then build features/backtests.** Use point-in-time timestamps, realistic costs, chronological validation, and a trial ledger; see [[Research workflow]] and [[Edge validation]].

### Minimal Python smoke test

```python
from lse import LSE

client = LSE()  # reads LSE_API_KEY from the environment
items = client.catalog("forex")
print(items[:5])  # inspect the exact available symbols and coverage metadata

# Replace with a symbol actually returned by the catalog.
sample = client.candles("EUR/USD", "1h", start="2024-01-01", end="2024-01-03")
print(len(sample), sample[:2])
```

For bulk history:

```python
from lse import LSE

client = LSE()
history = client.history("EUR/USD", timeframe="1h", start="2024-01-01", end="2024-02-01")
print(type(history), getattr(history, "shape", None))
```

Confirm the supported arguments in the installed SDK version before running examples; SDK methods and server policy may evolve.

## Useful access patterns exposed by the SDK

- `catalog(category)` / `datasets(...)`: discover instruments and coverage.
- `candles(...)`: bounded historical OHLCV queries.
- `series(...)`: macroeconomic or bond-yield series.
- Reference methods: economic calendar, insider trades, dividends, splits, COT, financial reports, company profiles, fundamentals, and bond yields.
- Options methods: chain, recent flow, and contract candles; the SDK notes some distinctions in historical coverage.
- `history(...)` / `dataset(...)`: bulk Parquet export jobs.
- `stream(...)` / `stream_async(...)`: WebSocket streaming; SDK docs describe replay availability up to 24h before continuing live.

The exact available datasets, query caps, history depth, symbol syntax, options data windows, and quotas are account/server-dependent and should be verified in a live small query.

The README now documents `catalog()` without arguments as returning the provider's full live catalog (advertised as 22,000+ rows) and category names including stocks, forex, crypto, ETF, commodity, index, options, futures, economics, bonds, volatility, interest rates, and currency index. These are provider claims, not a verified count of complete datasets. A catalog row indicates a listed dataset/symbol, not that every timeframe, date range, contract history, or reference set is complete. See [[Exhaustive dataset inventory and transformation protocol]] before planning a full export.

## Research suitability and verification checks

LSE's public pages/README make large coverage and free-access claims. Treat those as vendor assertions until tested. In particular:

- **Coverage:** check data per instrument and dates. An advertised class count does not imply complete history for each name.
- **Accuracy and completeness:** compare sample observations against an official exchange, regulator, or reputable independent vendor; measure missingness, stale values, duplicates, and revisions.
- **Survivorship and point-in-time behavior:** ask whether historical universe membership, symbol changes, delisted securities, corporate actions, and revised macro values are represented as they were known then.
- **Tick/candle semantics:** determine whether timestamps identify trade, bar start, bar close, or collection time; clarify timezone and aggregation rules.
- **Volume and market fragmentation:** FX/crypto and other fragmented markets may not have a consolidated volume figure; inspect the venue/feed definition.
- **Terms:** confirm research, commercial-use, retention, internal-sharing, and derived-data permissions from current terms before use.
- **Reproducibility:** record package version, query, retrieval date, schema, and a local hash where permitted.

Use LSE as a discovery and research data source, then independently validate any result that will support a strong claim. A free dataset is especially useful for prototyping, not a substitute for lineage checks.

## Pipeline integration pattern

Treat each LSE API/export operation as an acquisition stage, not as an implicit canonical dataset. Record the exact symbol, category/dataset, timeframe, date bounds, package version, retrieval timestamp, returned schema/count, and terms with the raw response/export. Validate that pagination or export completed, that timestamp conventions and units are correct, and that a final candle is complete before transforming it. Keep provider snapshots separate from normalized tables and experiment features; see [[Research pipeline architecture]] and [[Data validation patterns]].

### Research smoke-test gates

Before a broader request, confirm: (1) catalog entry and coverage for the exact symbol; (2) installed package version and method signatures; (3) key authentication without printing or logging the secret; (4) response status, row count, schema, timezone/bar semantics, and final-bar completion; (5) one independent price comparison; and (6) current account quota and data terms. A successful API response establishes access for that query, not accuracy, completeness, point-in-time history, or permission for third-party sharing.

For a full metadata catalog snapshot before selecting any bulk history, follow [[Tools/Inventory LSE catalog]]. Its linked helper prompts locally for the API key and calls only `catalog()`; it does not fetch market-history rows.

## Primary references

- [London Strategic Edge data portal](https://londonstrategicedge.com/data) — provider's data and access entry point. **Grade 5** for its own feature/access claims; not independent evidence of data quality.
- [API documentation](https://londonstrategicedge.com/api-documentation) — official endpoint reference; JavaScript rendering may prevent complete text extraction in some clients. **Grade 5** for product/API behavior.
- [Terms of Service](https://londonstrategicedge.com/terms) — review current terms before use. **Grade 5** for provider's contractual terms; obtain legal guidance as needed for institutional use.
- [Public `lse-data` SDK README](https://github.com/londonstrategicedge/lse-data) — setup, examples, methods, data claims, and licensing note. **Grade 5** for SDK behavior; vendor-published coverage claims should be independently tested.
- [SDK `pyproject.toml`](https://github.com/londonstrategicedge/lse-data/blob/main/pyproject.toml) — Python version and dependency metadata. **Grade 5** for package metadata.
- [[Market data]] · [[Feature engineering]] · [[Forex]] · [[Crypto]] · [[ETFs]] · [[Options]]

## Copyright and files

No article or proprietary dataset was copied into the vault. SDK/package source is linked to its public repository; follow that repository's license for code. The market data's license is separate and its terms restrict redistribution. The user can provide source files that they are licensed to share, if needed for the research environment.
