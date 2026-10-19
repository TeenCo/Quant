# Quantitative Research Obsidian Vault — Plan

> **Vault folder:** `Research` (Obsidian vault name: `research`)

## Purpose

Build a deep, linked educational and research vault for interns learning to develop, research, and test ideas. The broad scope includes economics and quantitative methods, with the primary emphasis on quantifying data, identifying statistically credible market edges, and understanding how edges may decay.

Collect a wide range of material, including less conventional or obscure leads. Preserve the distinction between a novel hypothesis and evidence that supports it: unusual correlations may inspire research, but must be labeled and tested rather than presented as established alpha.

## Source and evidence policy

- Search broadly across academic research, textbooks, lecture notes, technical writing, datasets, and documented practitioner accounts.
- Classify source claims on a **1–10 evidence/provenance scale** (lower is stronger). Grade 1 is a recent, reputable peer-reviewed/academic or primary-source item with transparent methodology, accessible provenance, and independently checkable evidence. Grades 2–3 are strong academic/official sources with minor caveats or early-stage status; grades 4–6 are useful but more limited, older, indirect, or methodologically incomplete; grades 7–8 are trade/practitioner and secondary material with partial verification; grades 9–10 are anecdotal stories, opaque claims, or unverified leads. The grade applies to the source's support for a specific claim, not to whether the idea deserves exploration.
- Keep **evidence grade**, **recency**, and **novelty** as separate fields. A dated foundational result may remain high-quality evidence; a recent vendor claim is not high-quality evidence simply because it is current.
- Record publication/update date, author or institution, source type, methods, limitations, and a direct link wherever available.
- Treat recency and reliability as separate considerations: an older foundational result can remain valuable, and a recent anecdote is not strong evidence merely because it is recent.
- Summarize and link copyrighted works. Include local copies only when distribution is permitted. Flag useful works that require the user to provide a copy.
- Include a practical London Strategic Edge data-source walkthrough, verifying access requirements, dependencies, data formats, quotas, and workflow against current official documentation and repository source.

## Vault structure

Create a navigable `index.md` and a running `log.md`, then organize substantial subject areas into linked topic notes and subtopics. Keep market-specific material in dedicated folders and cross-link it to shared methods and concepts.

### Core areas to cover

- Mathematics: linear algebra, multivariable calculus, probability, statistics, optimization, and multidimensional geometry/topology.
- Econometrics and economics: time series, causal inference, forecasting, market and macroeconomic data, and empirical methods.
- Machine learning: supervised and unsupervised learning, deep learning, LSTMs and sequence methods, reinforcement learning, and applications to financial data.
- Research practice: data quality, feature construction, backtesting, validation, multiple testing, leakage, overfitting prevention, statistical significance, robustness, and edge decay.
- Engineering: efficient data workflows, profiling, runtime reduction, code execution and numerical optimization, reproducibility, and research pipelines.
- Data and alternative hypotheses: document provenance, transformations, limitations, and evidence quality; retain unconventional leads with clear uncertainty labels.

### Market folders

Create dedicated folders for at least:

- Forex
- ETFs
- Crypto
- Equities
- Futures
- Options
- Fixed income
- Commodities

Add further markets when useful. Each market area should cover relevant data, instruments, market structure, research considerations, and links to shared methods.

## Progress checklist

### Planning and structure

- [x] Capture the vault goals and scope.
- [x] Define source/evidence grading principles and copyright handling.
- [x] Specify the index, research log, and linked-note organization.
- [x] Specify market-specific folders.
- [x] Agree on a working source-grade rubric (1 strongest to 10 weakest; evidence, recency, and novelty recorded separately).
- [x] Create the folder structure and starter navigation files inside the `Research` vault.
- [x] Create `index.md`, `log.md`, shared topic folders, and dedicated folders/notes for Forex, ETFs, Crypto, Equities, Futures, Options, Fixed Income, and Commodities.

### Research and content

- [x] Inventory core topics and build an initial linked curriculum map.
- [x] Research and document London Strategic Edge, including dependencies and a step-by-step data-use walkthrough.
- [x] Collect and grade an initial group of sources across quantitative methods, ML, finance, research engineering, and data.
- [x] Develop first-pass topic notes and subtopic notes with summaries, links, limitations, and cross-links.
- [x] Expand edge-validation material with inferential pitfalls, alternative-data design, economics-to-market mapping, exercises, and additional academic research leads.
- [x] Add a microstructure/high-frequency research pass covering book reconstruction, execution costs, event models, and source-grounded exercises.
- [x] Add a primary financial/economic data-source directory and detailed point-in-time, vintage, identifier, revision, and access guidance.
- [x] Add an alternative-data opportunity map, physical-supply-chain case study, source notes, and an evaluation checklist.
- [x] Add practical ingestion architecture, schema validation, experiment tracking, and reproducibility guidance.
- [x] Deepen time-series research with forecast comparison, structural instability, volatility forecasting, and a practical stability exercise.
- [x] Add an options-market research pass on implied volatility, variance risk premia, VIX, data limitations, and a forecast-to-trading exercise.
- [x] Deepen existing statistical inference, forecast evaluation, probability, overfitting, and financial ML validation notes with derivations and worked examples.
- [x] Deepen existing mathematics, economics/econometrics, ML, research methods, data, engineering, and eight market workspaces with worked derivations, examples, and validation guidance.
- [x] Populate market folders with market-specific instrument conventions, data requirements, hypotheses, and validation exercises.
- [x] Break current broad topics into hyper-specific linked subnotes and research subtopics that lacked concrete derivations, data semantics, or validation exercises.
- [x] Broaden data coverage with global macro/national statistics, cross-market reference and public market data, and satellite/transport/agriculture/activity sources with access and point-in-time caveats.
- [ ] Enumerate the authorized London Strategic Edge catalog, reconcile all listed dataset/instrument/timeframe coverage, and transform acquired records only after access, quota, licensing, and completeness are verified.
- [x] Snapshot and profile the authorized LSE catalog metadata; document coverage, schema limits, anomalies, and staged acquisition criteria.
- [ ] Retrieve current LSE vault metadata, reference inventory, and account usage through the local preflight helper; use the result to size representative test exports.
- [x] Compare a second authorized LSE catalog snapshot and build a local, bounded representative sample plan without requesting data.
- [x] Retrieve timestamped vault metadata, reference inventory, and account usage; define an opt-in schema sample capped at 3 rows per call.
- [x] Run bounded endpoint schema samples with user confirmation and record response fields, request outcomes, basic QC, and a blocking freshness anomaly.
- [x] Normalize the bounded endpoint samples into a local lineage-preserving proof of concept; retain raw rows and record transformation/QC manifest.
- [x] Build resumable, safety-capped local runners for the selected daily-candle/series scope and the separate reference-export queue.
- [ ] Run full daily candles/series acquisition in bounded batches; reconcile every catalog task as complete, empty, blocked, or excluded.
- [ ] Reconcile blocked `stocks/VCTR` HTTP 500 after remaining daily/series tasks; verify endpoint/source or document as excluded.
- [x] Run and validate first bounded daily-candle ingestion pilot; preserve resume state and document QC.
- [ ] Run prioritized date-partitioned reference exports within weekly/monthly byte caps; reconcile all reference inventory partitions.
- [ ] Resolve LSE option-chain stale/expired results with provider documentation/support and independent data before using chain data; validate other families against independent sources before full transformation.
- [x] Inventory accessible online texts/PDF links and flag local copies that require licensing or user-provided material.
- [x] Preserve unconventional and obscure leads as explicit hypotheses with evidence limits, source grades, and falsification/validation requirements.

### Review and maintenance

- [x] Check wiki-links, source metadata, and grade consistency for current notes.
- [x] Record collection and review activity in append-only `log.md`.
- [x] Keep the index usable and link the newly deepened content.
- [x] Index the atomic subtopic notes by discipline, market, research design, and engineering.

### Completion boundaries

- [x] Document current source access, licensing, and point-in-time limitations; no restricted data or copyrighted papers were copied.
- [ ] If local copyrighted copies are desired, user provides files they are licensed to share; otherwise use linked online materials.
- [ ] For any empirical project, validate market-data SDKs/feeds using the user's credentials and intended account entitlements; the vault documents a walkthrough but makes no live claims about account access or observed data quality.
- [ ] Strategy-specific empirical replications are project-dependent; the vault is a research curriculum and does not establish a deployable edge.

## Research log

Treat `log.md` as append-only: add every entry at the end with an ISO 8601 timestamp and timezone; never edit or delete previous entries. Record areas reviewed, sources added, structural/grading decisions, blockers, corrections (as new entries), and next steps. Keep this checklist updated alongside the log.
