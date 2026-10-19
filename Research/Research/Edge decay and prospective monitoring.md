# Edge Decay and Prospective Monitoring

## Distinguishing explanations

Decline may reflect noise, exposure change, measurement drift, worse execution, crowding, or mechanism decay. These are hypotheses, not interchangeable diagnoses. A descriptive model \(\mu_t=\mu_0e^{-\lambda(t-t_0)}\) summarizes decay but does not identify its cause. If forecast calibration is stable while spread/shortfall worsens, execution deterioration is more plausible than forecast decay.

Before prospective outcomes, fix cadence, metrics, minimum sample, control limits, actions, and retraining policy. Repeated looks require sequentially valid alarms or appropriate multiplicity treatment; do not reset thresholds after seeing results.

## Failure modes

- Many windows/metrics yield uncorrected alert fishing.
- Thresholds reset to preserve the strategy.
- Short noisy run is declared regime change.
- Retrained policy's returns are attributed to original model.
- Discovery-to-deployment delay ignored.

## Falsifiable exercise

Freeze a quarterly rule, then prospectively test it without threshold edits. Simulate stable data and injected shifts separately in forecast mean, cost, and feature distribution. The monitoring design fails if stable-data false alarms exceed its declared rate or relevant shifts are not detected within its promised horizon.

## Graded sources

- **Grade 1, sequential method:** Page (1954), “Continuous Inspection Schemes.” [DOI](https://doi.org/10.1093/biomet/41.1-2.100). CUSUM foundations; operating properties depend on assumptions/tuning.
- **Grade 1, methods text:** Basseville & Nikiforov (1993), *Detection of Abrupt Changes*. [Bibliographic record](https://books.google.com/books?id=Ef7jBwAAQBAJ). General change detection, not market-edge decay evidence.
- **Grade 2, hypothesis only:** Crowding may erode returns; declining performance alone does not establish crowding. Require independent crowding/liquidity measures.

Related: [[Edge validation]] · [[Research workflow]] · [[Overfitting controls]]
