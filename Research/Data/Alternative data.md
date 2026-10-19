# Alternative Data and Unconventional Hypotheses

Alternative data can generate useful questions when it measures activity not yet fully reflected in standard market data. Novelty is a search advantage, not proof of predictive value.

## Lead-generation framework

For each dataset, record its real-world generating process, collector, universe, time coverage, publication/arrival delay, revisions, sampling bias, representativeness, missingness, and license. Form a mechanism: what latent economic behavior could it measure, who might observe it, and how quickly could trading reflect it?

## Candidate families

- Web/search attention, app usage, product pricing, job postings, reviews, and web traffic.
- Text/news, filings, corporate disclosures, public statements, and social networks.
- Shipping, port congestion, flight activity, satellite imagery, weather, energy loads, and agricultural signals.
- Public government records, procurement, customs, regulatory data, and corporate registries.
- On-chain activity, exchange flows, funding/basis, protocol usage, and network measures.
- Calendar, payments, transaction aggregates, and consumer demand proxies where lawful and appropriately licensed.

## Key questions and hazards

- Is the data available in real time or only retrospectively? Was its historical version backfilled?
- Is it a measure of the economic activity or of media attention/measurement intensity?
- Could the signal proxy for known exposures, size, geography, sector, seasonality, or changing coverage?
- Are collection methods stable and independent of the price outcome?
- Do data terms allow research, commercial use, retention, and derived outputs?
- Can an effect survive multiple testing, cross-validation, latency, cost, and a plausible independent dataset?

Keep speculative stories at low grades in [[Source grading]]. Preserve them in a lead ledger with explicit falsification criteria. See [[Edge validation]], [[Feature engineering]], and [[Research workflow]].

For a detailed design sequence, see [[Alternative-data research design]]. For translating a causal/economic mechanism to market outcomes, see [[Economics-to-market hypotheses]].

## Measurement error and representativeness

Let latent activity be \(A_t\) and observed proxy \(X_t=A_t+u_t\) in a simple measurement-error model. If noise \(u_t\) is independent classical error, linear predictive slopes may be attenuated; in practice, coverage error is often nonclassical and correlated with activity, geography, attention, or market outcomes. A satellite detector may observe cloud-free scenes more often in certain regions; a search index may be normalized to sampled queries; AIS may undercount vessels with weak receiver coverage. Document the observation mechanism rather than assuming a proxy is a noisy but unbiased measure.

## Vendor backfill and survivorship

Historical alternative-data archives may be reconstructed using current entity mappings, current model outputs, or only records that remain commercially valuable. Request version/coverage history and test the historical availability of each record. A vendor's present-day historical feed is not automatically point-in-time. If availability history cannot be verified, label tests exploratory and avoid claims of historical tradability.

## Staged acquisition protocol

1. Read documentation/terms and identify permitted storage, derived use, and redistribution.
2. Obtain a small, representative sample covering normal and failure periods.
3. Compare observations with an independent/official proxy and quantify missingness/latency.
4. Freeze a feature definition and timestamp rule before broad modeling.
5. Preserve a record of source/version changes and failed/null trials.

This protects research validity and reduces compute spent on feeds that cannot support the intended question.
