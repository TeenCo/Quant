# Quantitative Research Vault

> **Research aim:** Learn to turn broad economic and market data into testable hypotheses, distinguish real predictive information from noise and bias, and measure whether an apparent edge can survive costs, regime changes, and competition.

The vault is a growing curriculum and research library, not a catalogue of guaranteed strategies. Unusual correlations and obscure datasets are welcome as **hypothesis generators**; results are only promoted when their provenance, statistical validity, and economic plausibility hold up.

## Start here

- [[Plan|Vault plan, scope, and progress checklist]]
- [[log|Append-only research activity log]] — timestamp every addition; corrections are new entries.
- [[Research workflow|End-to-end research workflow]]
- [[Source grading|Source grades and evidence policy]]
- [[Data/London Strategic Edge|London Strategic Edge: data access and dependencies walkthrough]]
- [[Edge validation|How to assess a potential statistical edge]]
- [[Statistical inference for trading|Statistical inference, dependence, and trading significance]]
- [[Statistical testing pitfalls|Common traps in statistical tests on market data]]
- [[Alternative-data research design|Testing unusual/obscure data leads without losing rigor]]
- [[Alternative data opportunity map|Alternative-data families and source leads]]
- [[Alternative data experiment design checklist|Checklist for evaluating new alternative-data ideas]]
- [[Alternative data case study - physical supply chain|Worked research design: shipping and commodity flows]]
- [[Economics-to-market hypotheses|Mapping economic mechanisms into testable market questions]]
- [[Research exercises|Hands-on research-design and inference exercises]]
- [[Research pipeline architecture|Repeatable acquisition-to-report data pipeline]]
- [[Experiment reproducibility|Run manifests and reproducibility levels]]
- [[Data validation patterns|Structural, temporal, and domain validation]]
- [[Experiment tracking implementation notes|Tracking tools and run protocol]]
- [[Financial data source directory|Primary data sources by topic and market]]
- [[Sources/Global macro and national statistics sources|Global macro and national statistical sources]]
- [[Sources/Cross-market reference prices and public market data|Cross-market reference prices and public market-data access]]
- [[Sources/Official satellite, transport and activity datasets|Satellite, agriculture, aviation, port and activity datasets]]
- [[Data provenance and point-in-time|Data lineage, vintages, corrections, and quality controls]]
- [[Exhaustive dataset inventory and transformation protocol|Full-catalog inventory, acquisition reconciliation, and validated transformation workflow]]
- [[LSE catalog coverage review 2026-10-18|Authorized catalog snapshot: coverage, anomalies, and staged transformation plan]]
- [[LSE daily series acquisition pilot|First bounded daily-candle ingestion pilot and QC]]
- [[LSE bounded schema sample findings 2026-10-18|Sampled LSE endpoint schemas and options-chain freshness anomaly]]
- [[Tools/Inventory LSE catalog|LSE metadata-only catalog inventory helper and run instructions]]
- [[Tools/lse_metadata_preflight.py|LSE metadata and quota preflight helper]]
- [[Tools/build_lse_sample_plan.py|Build a bounded, review-only representative sample plan]]
- [[Tools/Sample LSE endpoint schemas|Opt-in bounded samples to inspect actual endpoint schemas]]
- [[Tools/sample_lse_dataset_endpoints.py|Bounded local endpoint sampler script]]
- [[Tools/normalize_lse_bounded_samples.py|Normalize bounded samples with lineage and raw-record preservation]]
- [[Tools/Run LSE daily series sync|Preview/resume all cataloged daily candles and series in bounded calls]]
- [[Tools/Plan and run LSE reference exports|Partition and resume quota-aware reference-table Parquet jobs]]
- [[Data vintage and real-time testing|Point-in-time joins and revision-aware backtesting]]
- [[Survivorship, identifiers and universe|Historical universes, security lifecycles, and stable IDs]]
- [[Forecast evaluation|Forecast scoring, benchmarks, and model comparison]]
- [[Mathematics/Statistics|Worked derivations: dependence-aware uncertainty and Sharpe scaling]]
- [[Statistical inference for trading|Inference in finance: dependence, selection, and economic hurdles]]
- [[ML validation|Purging, embargo, nested chronological evaluation, and worked split example]]
- [[Structural breaks and parameter instability|Regime shifts, drift, and adaptation choices]]
- [[Volatility models|Conditional risk and volatility forecasting]]
- [[Markets/Options/Implied volatility, variance risk premium and VIX|Options: implied volatility, variance risk premium, and VIX]]
- [[Sources/Cboe VIX methodology and data|Cboe VIX methodology and data source assessment]]
- [[Research/Options volatility exercise|Options volatility: forecast and strategy-design exercise]]
- [[Regime-stability and forecast comparison exercise|Hands-on forecast and stability exercise]]
- [[High-frequency data research|High-frequency market data research design]]
- [[Microstructure exercises|Hands-on execution and order-book exercises]]

## Deepened reference set

- [[Mathematics/Linear algebra|Linear algebra: least squares, conditioning, shrinkage, and PCA]]
- [[Mathematics/Calculus and optimization|Optimization: constrained allocation, KKT checks, and gradient verification]]
- [[Mathematics/Topology and geometry|Geometry/topology: metric selection, embeddings, and null design]]
- [[Probability|Probability: conditional expectation, martingales, and tail risk]]
- [[Mathematics/Statistics|Statistics: dependence-aware uncertainty and Sharpe scaling]]
- [[Econometrics/Time series|Time series: AR dynamics, stationarity, cointegration, and calendars]]
- [[Causal inference|Causal inference: potential outcomes, design assumptions, and event studies]]
- [[Machine learning/Supervised learning|Supervised ML: losses, regularization, and target design]]
- [[Machine learning/Sequence models|Sequence models: LSTM equations and temporal alignment]]
- [[Markets/Forex/Forex|Market notes: Forex]] · [[Markets/ETFs/ETFs|ETFs]] · [[Markets/Crypto/Crypto|Crypto]] · [[Markets/Equities/Equities|Equities]] · [[Markets/Futures/Futures|Futures]] · [[Markets/Fixed Income/Fixed Income|Fixed income]] · [[Markets/Commodities/Commodities|Commodities]] · [[Markets/Options/Options|Options]]
- [[Data provenance and point-in-time|Data as-of joins and lineage]] · [[Research pipeline architecture|Pipeline recovery and contracts]] · [[Performance|Profiling and determinism]]
- [[Research/Reading access and local assets|Open online readings, local-copy permissions, and copyrighted material flags]]

## Hyper-specific subtopic notes

### Mathematics

- [[Conditional expectation and forecasts]] · [[Limit laws for dependent returns]] · [[Statistical estimation and inference]]
- [[Regression covariance and PCA]] · [[Convexity and constrained optimization]] · [[Persistent homology for market data]]
- [[Portfolio construction and estimation risk]]

### Economics and econometrics

- [[ARIMA and Kalman filtering in real time]] · [[Cointegration estimation and error correction diagnostics]]
- [[GARCH estimation and residual diagnostics]] · [[Break alarms and real-time adaptation]]
- [[Difference-in-differences for market events]] · [[Macro mechanism to market data and vintages]]

### Machine learning

- [[Supervised loss and calibration]] · [[Boosting and regularization]] · [[Clustering and HMM state inference]]
- [[Deep learning regularization and attention]] · [[LSTM and state-space forecasting]] · [[RL off-policy evaluation]]

### Market-specific mechanics

- FX: [[FX carry and forward parity]]
- ETFs: [[ETF NAV creation and basket mechanics]] · [[Daily leveraged ETF reset and path dependence]]
- Crypto: [[Perpetual funding and venue clocks]]
- Equities: [[Corporate actions and filing event clocks]]
- Futures: [[Futures roll execution and curve carry]]
- Fixed income: [[Bond duration curve and credit decomposition]]
- Commodities: [[Storage location inventory and curve mapping]]
- Options: [[Volatility surface Greeks and event variance]]

### Research design

- [[Selection-aware inference for strategy search]] · [[Point-in-time feature availability contract]]
- [[Forecast value and decision mapping]] · [[Market event studies and causal identification]]
- [[Execution cost validation protocol]] · [[Alternative-data measurement and negative controls]]
- [[Historical-universe reconstruction and delisting outcomes]] · [[Edge decay and prospective monitoring]]

### Data and engineering

- [[Bitemporal versioned joins]] · [[Identifier and security master lifecycle]]
- [[API quotas retries and raw snapshots]] · [[Schema domain temporal validation]]
- [[Data contracts and lineage]] · [[Profiling vectorization and chunking]]
- [[Manifests tracking security and licensing]]

## Curriculum map

### Quantitative foundations

- [[Mathematics|Mathematics for quantitative research]]
  - [[Mathematics/Linear algebra|Linear algebra and matrix methods]]
  - [[Mathematics/Calculus and optimization|Multivariable calculus and optimization]]
  - [[Mathematics/Probability|Probability and stochastic processes]]
  - [[Mathematics/Statistics|Statistical inference and estimation]]
- [[Mathematics/Topology and geometry|Multidimensional geometry and topology]]
- [[Economics|Economics and macro foundations]]
- [[Econometrics|Econometrics and empirical methods]]
  - [[Time series|Time series, dependence, and forecasting]]
  - [[Causal inference|Causal inference and identification]]

### Markets, data, and signals

- [[Market data|Market data: structure, provenance, and pitfalls]]
- [[Market microstructure|Market microstructure, execution, and liquidity]]
  - [[Order book data and event-time reconstruction|Order book feeds and event-time reconstruction]]
  - [[Execution costs and market impact|Execution costs, shortfall, and capacity]]
  - [[Order flow and event models|Order flow, Hawkes processes, and event models]]
- [[Data/Alternative data|Alternative data and unconventional hypothesis generation]]
- [[Feature engineering|Feature construction and point-in-time correctness]]
- [[Edge validation|Statistical edges, costs, robustness, and decay]]

### Machine learning

- [[Machine learning|Machine learning in financial research]]
  - [[Supervised learning|Supervised learning]]
  - [[Unsupervised learning and regimes|Unsupervised learning and regimes]]
  - [[Deep learning|Deep learning]]
  - [[Sequence models|LSTM and sequence models]]
  - [[Reinforcement learning|Reinforcement learning]]
  - [[ML validation|Financial ML validation and leakage controls]]

### Research and engineering

- [[Research workflow|Research workflow and experiment design]]
- [[Overfitting controls|Overfitting, multiple testing, and selection bias]]
- [[Performance|Runtime reduction and code execution optimization]]
- [[Research pipelines|Reproducible data and model pipelines]]
- [[Data dictionary and provenance card|Template for recording source metadata and quality checks]]

## Market-specific workspaces

Each market note links its data, structure, instruments, and applicable research methods to shared foundational notes.

- [[Forex]]
- [[ETFs]]
- [[Crypto]]
- [[Equities]]
- [[Futures]]
- [[Options]]
- [[Fixed Income]]
- [[Commodities]]

## Research library: first-pass reading list

The source grade is a working assessment of how strongly an item supports the relevant claim, not a ranking of its intellectual importance. Read the source note for caveats and further links.

- [[Sources/Harvey Liu Zhu 2016|Harvey, Liu & Zhu (2016): factor discovery and multiple testing]] — **Grade 2**
- [[Sources/Novy-Marx 2015|Novy-Marx (2015): combining signals and backtest overfitting]] — **Grade 2**
- [[Sources/Athey Imbens 2017|Athey & Imbens (2017): applied econometrics and causal inference]] — **Grade 2**
- [[Sources/Miyato Dai Goodfellow 2017|Miyato, Dai & Goodfellow: adversarial regularization]] — **Grade 2**
- [[Sources/Carr Lopez de Prado 2014|Carr & López de Prado: reduce backtest configuration search]] — **Grade 3**
- [[Sources/Bacry Mastromatteo Muzy 2015|Bacry et al.: Hawkes processes in finance]] — **Grade 2**
- [[Sources/Moreira Muir 2017|Moreira & Muir: volatility-managed portfolios]] — **Grade 2**
- [[Sources/Davis Fuenzalida Taylor 2019|Davis et al.: macro-finance and market-implied r*]] — **Grade 2**
- [[Sources/Rolnick et al 2019|Rolnick et al.: climate and ML data opportunity map]] — **Grade 3**
- [[Sources/Official alternative-data sources|Primary and commercial source notes for physical and public data]]
- [[Sources/Diebold Mariano 1995|Diebold–Mariano: comparing forecast accuracy]]
- [[Sources/Forecasting Principles and Practice|Hyndman & Athanasopoulos: forecasting textbook]]
- [[Sources/Obizhaeva Wang 2005|Obizhaeva & Wang: dynamic supply/demand and execution]] — **Grade 2**
- [[Sources/Fisman Hamao Wang 2014|Fisman et al.: geopolitical shocks and firm exposure]] — **Grade 2**
- [[Sources/Financial ML field notes|Financial ML validation: purging, embargo, and backtest selection]] — **Grade 4; methodological reading lead**
- [[Sources/LSE data SDK|London Strategic Edge data SDK and source claims]] — **Grade 5 for platform access facts; unverified for data quality/performance claims**

## Source grade legend

| Grade | Typical interpretation |
|---|---|
| 1 | Recent, independently verifiable peer-reviewed or authoritative primary evidence; transparent data and methods. |
| 2–3 | Strong academic, official, or technically documented sources, with some limitation (e.g. working paper or older but still applicable). |
| 4–6 | Useful evidence or methods with notable constraints, indirectness, limited replication, age, or vendor/practitioner perspective. |
| 7–8 | Secondary, trade, practitioner, or descriptive material with partial verification; useful for leads and context. |
| 9–10 | Anecdotal, opaque, story-based, or otherwise unverified claims; preserve as leads, not established evidence. |

Record the separate **recency**, **source type**, **novelty**, and **limitations**. See [[Research/Source grading]].

## Vault conventions

- Topic notes summarize concepts and link to neighboring disciplines, methods, datasets, and markets.
- Source notes preserve citation details, grade, source links, summary, caveats, and follow-up leads.
- Copyrighted books and papers are linked and summarized; only freely distributable copies are saved locally. Items requiring a user-provided copy are flagged.
- Market notes explicitly state the instrument universe, venue, time zone, timestamp semantics, survivorship risks, and data licensing where known.
- Use [[log]] to record dated research progress and update [[Plan|the checklist]] as the vault grows.
