# Forecast Evaluation and Decision Mapping

## Derivation and example

Forecast quality and decision value are different estimands. Under a simple mean-variance objective, target exposure is \(q^*=\hat\mu/(\gamma\sigma^2)\); with turnover cost \(c|q-q_{prev}|\), a positive forecast may rationally imply no trade. A +4 bp forecast with 3 bp round-trip cost and 5 bp forecast error is not established positive net value.

Score forecasts with a proper metric matching the forecast (e.g. squared error for means, log score for probabilities). Separately evaluate one frozen policy against no-trade/benchmark after costs and constraints, with chronological and dependence-aware uncertainty.

## Failure modes

- RMSE, direction accuracy, or calibration is presented as profitability.
- Forecast horizon/population differs from traded decision.
- Sizing, thresholds, or costs are tuned on test observations.
- State-dependent uncertainty and costs are ignored.

## Falsifiable exercise

Register forecast, policy map, and no-trade baseline. In a new chronological period report forecast loss/calibration and net utility separately. The decision-value claim fails if the locked policy does not beat baseline after costs even when forecast loss improves.

## Graded sources

- **Grade 1, established framework:** Gneiting & Raftery (2007), “Strictly Proper Scoring Rules, Prediction, and Estimation.” [DOI](https://doi.org/10.1198/016214506000001437). Scoring framework, not profitability evidence.
- **Grade 1, forecast comparison:** Diebold & Mariano (1995), “Comparing Predictive Accuracy.” [DOI](https://doi.org/10.1080/07350015.1995.10524599). Dependence assumptions matter.
- **Grade 1, economic forecast evaluation:** Granger & Pesaran (2000). [DOI](https://doi.org/10.1002/1099-131X(200009)19:7%3C537::AID-FOR797%3E3.0.CO;2-U). General distinction; application depends on decision setup.

Related: [[Research workflow]] · [[Statistical inference for trading]] · [[Edge validation]]
