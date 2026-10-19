# Market Event Studies and Causal Identification

## Estimand and example

An abnormal return may be defined as \(AR_{it}=R_{it}-(\hat\alpha_i+\hat\beta_i'F_t)\), with the baseline model fit outside the event window. This is descriptive unless a counterfactual and identification assumptions justify causal interpretation. For a scheduled 14:00 policy release, exact event time, anticipation, simultaneous news, and date-level clustering matter; a market move is not automatically the policy's causal effect.

Predefine event, treatment/surprise, counterfactual, clock, anticipation window, comparison units, confounders, and dependence cluster. For staggered treatments with heterogeneous effects, avoid naïve two-way fixed-effects event-study interpretation.

## Failure modes

- Daily event date hides pre/post timing.
- Events chosen after observing returns or endogenous to price action.
- Overlapping news contaminates window.
- Assets exposed to one event are treated as independent observations.
- Model residual is called causal without assumptions.

## Falsifiable exercise

Pre-register one scheduled release, primary short window, anticipation window, and matched placebo times. Use verified timestamps and date-clustered uncertainty. Mechanism weakens if placebo responses are similar or effect vanishes with accurate event ordering.

## Graded sources

- **Grade 1, foundational review:** MacKinlay (1997), “Event Studies in Economics and Finance.” [DOI](https://doi.org/10.1257/jel.35.1.13). Standard methods, not automatic causal identification.
- **Grade 1, causal methods:** Athey & Imbens (2017), “The State of Applied Econometrics: Causality and Policy Evaluation.” [DOI](https://doi.org/10.1257/jep.31.2.3). General guidance.
- **Grade 1, staggered designs:** Sun & Abraham (2021). [DOI](https://doi.org/10.1016/j.jeconom.2020.09.006). Specific concern: heterogeneous effects in staggered event-study panels.

Related: [[Statistical inference for trading]] · [[Research workflow]] · [[Economics-to-market hypotheses]]
