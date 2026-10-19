# Feature Engineering and Point-in-Time Data

Features encode observations into information a model or decision rule can use. In finance, the feature's economic and temporal meaning matters as much as its numeric transformation.

## Design questions

- What observation does the feature represent, and what mechanism connects it to the target?
- When was the value first observable to the simulated decision-maker?
- Is it revised, backfilled, restated, adjusted, or subject to publication delay?
- Does aggregation use event time, arrival time, exchange time, or vendor time?
- Is the feature missing because of data collection, market closure, or an economically meaningful zero?
- Does it encode market access, liquidity, survivorship, or future universe membership inadvertently?

## Good practice

- Define timezone, calendar, and event-time conventions explicitly; normalize timestamps but preserve original time and source.
- Store raw inputs immutably and keep transformation code/versioned.
- Build lags and rolling windows with strict backward-looking semantics.
- Apply scaling, imputation, winsorization, PCA, and selection only within the training fold.
- Point-in-time join fundamentals, macro releases, index membership, corporate actions, and alt data to the time they became available.
- For cross-sectional features, use the actual historical universe and document delisted/failed firms.
- Apply [[Data vintage and real-time testing]] to macro values, filing facts, and other revised or delayed series.
- Audit feature-target lead/lag relationships and compare with simple controls.
- Record source, coverage, revision behavior, licensing, freshness, and quality checks.

## Financial-data-specific transformations

Returns, volatility, volume, spreads, order imbalance, yield curves, carry, funding, basis, option-implied moments, calendar events, and macro surprises may all be candidate feature families. Each has distinct units, clocks, market conventions, and transaction-cost relevance. A transformation may change meaning across assets or regimes; normalize only with an explicit interpretation.

## Example: rolling z-score without future leakage

For raw feature \(x_t\), a rolling standardization is \(z_t=(x_t-\hat\mu_{t-1})/\hat\sigma_{t-1}\), where mean/scale use observations strictly available before the decision at \(t\). Choose window, minimum observations, and missing-value policy in advance; handle \(\hat\sigma=0\) explicitly. If a model uses fold-based standardization, fit parameters on training data and apply frozen parameters to validation/test within that fold. A full-sample z-score leaks future distribution information even though it does not use future labels.

## Feature contract

For every feature version, record definition/equation, source fields, unit, aggregation window, decision-time availability, time zone, missingness semantics, revision behavior, historical coverage, transformations, fit window, and expected economic mechanism. Store both source time and feature-ready time where processing latency matters. Use a no-feature baseline and ablations to estimate incremental value, but include those choices in trial accounting.

## Missingness and winsorization

Missing can mean unavailable, not applicable, market closed, zero activity, provider outage, or an economically meaningful absence. Do not collapse these into a single numeric zero without justification. Winsorization thresholds and imputation models must be fitted using past/training data; report sensitivity because extreme observations may be valid crash/liquidity events rather than errors.

See [[Market data]], [[Data provenance and point-in-time]], [[Survivorship, identifiers and universe]], [[Edge validation]], [[Time series]], [[London Strategic Edge]], and [[Research pipelines]].

For an explicit timestamp eligibility contract and vintage falsification, see [[Point-in-time feature availability contract]].
