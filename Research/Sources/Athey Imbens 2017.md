# The State of Applied Econometrics: Causality and Policy Evaluation

## Bibliography

- **Authors:** Susan Athey and Guido W. Imbens
- **Date / version:** arXiv:1607.00699, submitted 3 July 2016; published as a 2017 review.
- **Primary link:** [arXiv:1607.00699](https://arxiv.org/abs/1607.00699)
- **PDF:** [arXiv PDF](https://arxiv.org/pdf/1607.00699) — paper page notes its distribution license; check current license before placing a local copy.

## Assessment

- **Evidence grade:** 2 — scholarly methods review by leading econometricians; an overview rather than a single empirical study.
- **Recency:** 2017; valuable foundation, with newer developments to add for current practice.
- **Novelty:** Broad review of identification, robustness, and ML for causal effects.
- **Source type:** Academic review/preprint.

## Summary

The review discusses applied econometrics advances in program evaluation, including identification strategies such as synthetic controls and regression discontinuity; supplementary placebo, sensitivity, and robustness analysis; and ML approaches for high-dimensional adjustment and heterogeneous treatment effects.

## Research use and caveat

Financial prediction is often not a causal question. However, causal reasoning helps assess mechanism, confounding, event studies, and whether an apparent relationship is plausibly transportable. Markets can respond to anticipation, simultaneity, and changing equilibrium, so policy-evaluation designs require careful adaptation.

## How to use this review

Treat it as a map of applied causal-inference design choices, not as a recipe that makes observational data causal. For any method, identify its estimand and identifying assumption (e.g. continuity near a regression-discontinuity cutoff or parallel trends for difference-in-differences). Modern ML can help estimate nuisance functions or heterogeneity, but cannot manufacture exogenous treatment assignment. In financial settings, market anticipation, interference across firms/instruments, and equilibrium responses make the counterfactual especially substantive.

## Connected notes

[[Causal inference]] · [[Econometrics]] · [[Edge validation]] · [[Economics]]
