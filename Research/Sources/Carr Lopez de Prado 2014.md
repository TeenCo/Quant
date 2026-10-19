# Determining Optimal Trading Rules without Backtesting

## Bibliography

- **Authors:** Peter P. Carr and Marcos López de Prado
- **Date / version:** arXiv working paper submitted August 2014, revised September 2014.
- **Source:** [arXiv:1408.1159](https://arxiv.org/abs/1408.1159)
- **Full text:** [arXiv PDF](https://arxiv.org/pdf/1408.1159); arXiv page lists a non-exclusive distribution license. Verify the license if copying the file locally.

## Assessment

- **Evidence grade:** 3 — direct research paper with a formal setup and empirical/numerical evidence, but working-paper status, age, and model-specific result limit generality.
- **Recency:** 2014; methodological idea remains relevant; newer validation practices should be added.
- **Novelty:** Suggests deriving/calibrating trading rules from an assumed stochastic process rather than searching many configurations in a backtest.
- **Source type:** Working paper / arXiv preprint.

## Summary

The paper argues that calibrating rules by repeatedly comparing historical backtests can create selection bias and underperformance. It studies optimal rules under a discrete Ornstein–Uhlenbeck price process and reports numerical evidence for optimal solutions that can be computed without running alternative configurations through a conventional backtest engine.

## Limitations and research use

- The conclusion depends on the assumed process and setting; actual market dynamics may be nonstationary, non-OU, and subject to costs/constraints not captured by the simple model.
- “Without backtesting” does not mean “without empirical validation.” Any model-derived rule still needs out-of-sample and implementation testing.
- Useful as an alternative to brute-force parameter search and as a reminder to use theory/structure to reduce degrees of freedom.

## Connected notes

[[Overfitting controls]] · [[Statistical inference for trading]] · [[Time series]] · [[Research workflow]]
