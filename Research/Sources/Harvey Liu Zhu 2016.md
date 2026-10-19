# . . . and the Cross-Section of Expected Returns

## Bibliography

- **Authors:** Campbell R. Harvey, Yan Liu, Heqing Zhu
- **Date / version:** NBER Working Paper, October 2014; published in *Review of Financial Studies* 29(1), 2016, pp. 5–68.
- **DOI:** [10.1093/rfs/hhv059](https://doi.org/10.1093/rfs/hhv059)
- **Primary abstract / working paper:** [NBER Working Paper 20592](https://www.nber.org/papers/w20592)
- **Open full text:** NBER working paper landing page links a PDF; access and reuse terms are set by NBER/publisher. Not copied locally.

## Assessment

- **Evidence grade:** 2 — published peer-reviewed financial-economics methods paper, foundational for factor discovery discussion; publication age is a caveat for current factor counts and thresholds.
- **Recency:** 2016 publication; foundational, but pair with newer replication and methodological work.
- **Novelty:** High historical significance for the multiple-testing debate, though now widely cited.
- **Source type:** Peer-reviewed journal article; NBER working paper version.
- **Claim evaluated:** The scale of factor mining makes conventional significance thresholds inadequate; the paper proposes a framework that allows correlated tests and missing data and estimates higher hurdles for newly discovered factors.

## Summary

The authors study the large number of proposed factors in the cross-section of expected returns. Because researchers have tried many characteristics and specifications, a conventional single-test t-statistic threshold can produce false discoveries. Their framework estimates time-varying significance cutoffs while allowing dependence among tests and missing observations. The paper argues that new factors should face a substantially higher bar than the traditional `t > 2` convention.

## Limitations and research use

- The exact numerical hurdle depends on assumptions about the historical discovery process and effective trial count; do not convert it into a universal rule for every strategy class or sample.
- Factor literature is a specific setting; strategy search, intraday data, and non-equity signals have different dependence structures.
- Use it to motivate complete search logs, multiplicity-aware inference, and caution with reported novelty—not as a substitute for independent validation.

## Reading the result carefully

The paper is about discovery thresholds in a literature where candidate factors accumulate over time. Its central lesson is selection-aware: the nominal significance level for a single pre-specified test does not describe the evidence in a large, adaptive factor search. The proposed hurdle depends on assumptions about the trial process and dependence among tests. Use the framework as a prompt to reconstruct what was searched and to ask which discoveries are genuinely independent; do not transplant a headline t-statistic threshold to unrelated intraday or alternative-data searches.

## Practical translation

For an internal strategy project, enumerate the actual search dimensions (markets, horizons, features, costs, universes, transforms, model classes, stopping decisions). A complete experiment history may be more actionable than trying to infer an effective number of tests from a final result alone. Pair multiplicity treatment with point-in-time validation, dependence-aware uncertainty, and independent confirmation.

## Connected notes

[[Overfitting controls]] · [[Edge validation]] · [[Research workflow]] · [[ML validation]]
