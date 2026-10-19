# Selection-Aware Inference for Strategy Search

## Claim and derivation

Selecting the maximum among noisy estimates creates an optimistic estimate; this is established selection behavior. Under independent standard-normal null estimates, the expected maximum grows roughly as \(\sqrt{2\log m}\) for \(m\) trials (about 3 standard errors at 100 trials). Dependence changes the effective search size; undocumented/adaptive search makes it hard to know.

## Worked exercise

Generate 500 independent noise predictors for a noise return series. Select the highest absolute in-sample t-statistic and evaluate it on an untouched later sample. Repeat 1,000 times, then compare to a correlated-predictor design and nested chronological selection. Report all outcomes and null-selection rate.

## Failure modes

- Trial ledger omits plots, horizons, endpoints, or abandoned variants.
- Correction assumes a guessed number of independent tests.
- Repeatedly inspected holdout is still called untouched.
- Selection adjustment is mistaken for a remedy to leakage or execution errors.

## Falsifiable test

Pre-register the simulation design and threshold. A claimed selected effect must beat the selection-aware null in a fresh independent simulation/sample; otherwise the experiment supports winner's-curse explanation, not an edge.

## Graded sources

- **Grade 1, established method:** White (2000), “A Reality Check for Data Snooping,” *Econometrica*. [DOI](https://doi.org/10.1111/1468-0262.00152). Bootstrap test; inference depends on specified candidate universe and assumptions.
- **Grade 2, financial application:** Harvey, Liu & Zhu (2016), “...and the Cross-Section of Expected Returns,” *RFS*. [DOI](https://doi.org/10.1093/rfs/hhv059). Factor-literature hurdle is context-specific.
- **Grade 1, method:** Romano & Wolf (2005), “Stepwise Multiple Testing as Formalized Data Snooping,” *Econometrica*. [DOI](https://doi.org/10.1111/j.1468-0262.2005.00615.x). Stepwise family-wise procedure; validity depends on assumptions and test family.

Related: [[Overfitting controls]] · [[Statistical inference for trading]] · [[Edge validation]]
