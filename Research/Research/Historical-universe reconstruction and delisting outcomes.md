# Historical-Universe Reconstruction and Delisting Outcomes

## Why and how

At each rebalance time \(t\), build eligible set \(U_t\) from membership, listing status, liquidity, and identifiers available then. A current-survivor sample conditions on future survival; if failures have poor outcomes, this biases returns upward and risk downward. Example: today's index members backtested to 2000 answer a survivor-conditional question, not historical investability.

Use effective-dated security IDs/membership, retain IPOs and terminal events, distinguish issuer from share class, and include delisting consideration/returns. Mark unknown outcomes and bound sensitivity; never silently drop. Screens use trailing data only.

## Failure modes

- Reused ticker or share-class conflation.
- Current membership projected backward.
- Delisting return omitted.
- Future liquidity/price used in screens.
- Later corporate adjustment leaks into trade-time price.

## Falsifiable exercise

Freeze a portfolio rule and compare current constituents, effective-dated constituents with terminal outcomes, and conservative bounds for unknown delistings. Report coverage and results by formation year. If excess return vanishes under historical universe, survivorship is supported; otherwise this bias alone is insufficient.

## Graded sources

- **Grade 1, empirical evidence:** Shumway (1997), “The Delisting Bias in CRSP Data.” [DOI](https://doi.org/10.1111/j.1540-6261.1997.tb03818.x). Specific database/context; no universal correction factor.
- **Grade 1, primary data documentation:** CRSP US Stock & Indexes. [Official page](https://www.crsp.org/research/crsp-us-stock-indexes/). Scope documentation, not backtest validation.
- **Grade 2, internal synthesis:** [[Survivorship, identifiers and universe]].

Related: [[Survivorship, identifiers and universe]] · [[Feature engineering]] · [[Edge validation]]
