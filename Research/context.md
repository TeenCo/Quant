# Context for Future Agents

## Project

This is the `research` Obsidian vault, located in the `Research/` directory. It is being built as a broad educational and research library for interns, with the main focus on quantifying economic/market data, developing hypotheses, identifying statistically credible edges, and understanding implementation and edge decay.

The user has asked for an extensive, deeply linked vault covering mathematics, economics, econometrics, machine learning, financial applications, market microstructure, data, overfitting prevention, efficient code, statistical validation, and research pipelines. Unusual and obscure data/hypotheses are encouraged as research leads, but must not be presented as verified alpha without evidence.

## User requirements and decisions

- Broad economics and quantitative scope; prioritize quantifying data and potential market edges.
- Include diverse sources: academic papers, books, official data, technical docs, practitioner material, and stories/leads.
- Grade sources from **1 (strongest) to 10 (weakest)**. Grade evidence for a specific claim; record recency and novelty separately. Grade 1 means recent/reputable academic or primary evidence with transparent methods. Stories and unverified claims belong near grades 9–10.
- Respect copyright. Summarize/link non-open material; do not copy copyrighted articles or datasets. Flag materials that the user may provide.
- Obsidian structure includes `index.md`, `log.md`, linked topic/subtopic notes, and specific market folders.
- Market folders already established: Forex, ETFs, Crypto, Equities, Futures, Options, Fixed Income, Commodities.
- London Strategic Edge is a requested data source. Explain access, dependencies, and practical usage; keep provider claims distinct from independently established facts.
- Efficient methods are preferred, but correctness, reproducibility, realistic costs, and data provenance take priority over superficial speed.

## Important vault conventions

- `index.md` is the starting point and topic map; add links there when creating substantial new notes.
- `Plan.md` tracks scope and progress. Update relevant checkboxes when completing a new pass.
- **`log.md` is append-only.** Never edit or delete prior research entries. Append each addition at the end with an ISO 8601 timestamp and timezone. If correcting an earlier entry, append a correction that identifies it; preserve the original.
- Markdown note filenames sometimes contain spaces and capitalization. Obsidian wiki-links resolve by note basename; run a wiki-link check after batches of edits.
- Use `Sources/` for source summaries and bibliographic metadata; include grade, date/version, source type, claim scope, methods, limitations, and direct source links.
- Use `Data/Data dictionary and provenance card.md` when documenting a new dataset.
- No data or article downloads have been performed; existing content is link-and-summary based.

## Existing content at a glance

- **Research:** workflow, edge validation, overfitting/multiple testing, statistical inference/pitfalls, feature engineering, financial ML validation, alternative-data design, economics-to-market mapping, exercises, high-frequency research, and experimental regime/forecast comparison.
- **Mathematics:** linear algebra, multivariable calculus/optimization, probability, statistics, topology/geometry.
- **Economics/econometrics:** economics, causal inference, time series, forecasting evaluation, structural instability, volatility models.
- **Machine learning:** supervised/unsupervised learning, deep learning, sequence/LSTM, reinforcement learning.
- **Engineering:** research pipelines, performance, pipeline architecture, data validation patterns, experiment reproducibility/tracking.
- **Data:** London Strategic Edge walkthrough, alternative data, source directory, provenance/vintages, data-card template.
- **Markets:** market microstructure, order-book/event-time reconstruction, execution costs/impact, order-flow/Hawkes notes, and the eight market-specific workspaces.
- **Sources:** academic and official-source summaries including Harvey–Liu–Zhu, Novy-Marx, Athey–Imbens, Miyato et al., Carr–López de Prado, Bacry et al., Moreira–Muir, Davis et al., Rolnick et al., Obizhaeva–Wang, Fisman et al., Diebold–Mariano, and source documentation notes.

## Research already documented: recurring cautions

- Historical values are not necessarily point-in-time values. Record reference time, first publication/arrival time, vintage/revision, and receipt time separately.
- Official sources are authoritative for what they publish and their documented release/access policies, but not automatically for tradability or predictive utility.
- Vendor coverage, historical depth, completeness, and predictive claims need sample validation against independent sources.
- A forecast is not an edge until it survives selection-aware inference, chronological validation, realistic execution costs, capacity, and robustness tests.
- Data rights vary by source. SDK license does not imply data license; redistribution restrictions must be respected.
- Do not imply organizational affiliation or access to proprietary institutional data. Use public sources and documented user-provided material only.

## Current status and suggested next work

Several substantial first passes are complete, but the vault is still a first-pass curriculum rather than an exhaustive research library. Continue expanding depth with:

1. Derivations, worked examples, and exercises for core math/statistics/econometrics topics.
2. More source-grounded notes in forecasting, volatility, structural breaks, portfolio construction, causal inference, and execution.
3. Per-market source directories, instrument conventions, data calendars, and concrete validation examples.
4. Less common data-source leads with provenance, access, legal terms, latency, coverage, and falsifiable tests.
5. Critical follow-up/replication work for important or contested empirical results; do not overstate abstract-only review.

Before broad collection, keep source metadata, grades, and links organized; avoid duplicate source notes. Correct broken links and outdated access claims as newly discovered, using append-only corrections in `log.md`.

## Workflow for the next agent

1. Read `index.md`, `Plan.md`, and the latest entries at the end of `log.md` before choosing the next research area.
2. Review adjacent notes to avoid duplication and to identify missing cross-links.
3. Prefer primary academic/official documentation. Note whether full text or only an abstract/product page was actually reviewed.
4. Clearly distinguish established results, source/provider claims, inference, and speculative leads.
5. Add concise but substantive Obsidian notes, cross-link concepts and market applications, and update the index.
6. Update the plan checklist where appropriate.
7. Append a dated ISO 8601 entry to `log.md`; preserve all prior content.
8. Verify wiki-links and source URLs/access caveats before reporting completion.
