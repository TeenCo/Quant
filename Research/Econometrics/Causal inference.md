# Causal Inference and Identification

## Prediction is not causation

A variable may forecast returns without causing them; a causal effect may exist without providing a profitable forecast. State the estimand explicitly: prediction, policy effect, event response, treatment effect, or mechanism.

## Identification questions

- What comparison identifies the counterfactual?
- Which assumptions rule out confounding, anticipation, selection, or interference?
- Was the treatment/event time actually known when decisions could be made?
- Are units and treatment assignment measured consistently?
- Do placebo and sensitivity checks support the design?
- Is the result externally valid to other regimes, instruments, and market participants?

## Methods to study

Randomized experiments (where feasible), event studies, difference-in-differences, synthetic control, regression discontinuity, instrumental variables, matching/weighting, and causal ML for heterogeneous effects. Each relies on substantive assumptions.

## Finance-specific caution

Markets are forward-looking, endogenous systems. Public announcements are often anticipated; reactions may reflect confounders, selection, and changing equilibrium. Use careful timing, controls, placebos, and market microstructure context. See [[Sources/Athey Imbens 2017]].

## Potential outcomes and identification

Let \(Y_i(1)\) and \(Y_i(0)\) be unit \(i\)'s outcomes under treatment and control. The individual causal effect \(Y_i(1)-Y_i(0)\) cannot usually be observed because only one state occurs. Identification relies on assumptions that relate observed treatment assignment to the missing counterfactual. Random assignment can make treatment independent of potential outcomes in expectation; observational designs require explicit conditional independence, exclusion, continuity, parallel-trends, or other design-specific assumptions.

### Difference-in-differences example

For the market-event design, treatment timing, event-specific controls, and placebo exercise see [[Difference-in-differences for market events]].

For treated and comparison groups before/after an event, the basic contrast is

\[
\hat\tau=(\bar Y_{T,post}-\bar Y_{T,pre})-(\bar Y_{C,post}-\bar Y_{C,pre}).
\]

It removes common time changes and fixed group differences only under assumptions including parallel counterfactual trends, no differential concurrent shock, no anticipation (or a correctly modeled anticipation window), stable composition, and no spillover that changes the control group. Plot pre-event paths and use placebo dates/outcomes, but failure to reject pre-trend differences is not proof of parallel trends. With staggered treatment timing and heterogeneous effects, conventional two-way fixed-effects estimators can mix comparisons in problematic ways; use estimators aligned to the treatment structure and estimand.

## Event studies are not automatically causal

An event study estimates outcomes around a timestamp. It is descriptive unless the event timing and comparison design identify a counterfactual. In markets, event windows must account for announcement time, leakage/rumors, overlapping news, trading hours, auction effects, bid-ask bounce, and event clustering. Returns before the timestamp may indicate anticipation or timestamp error; post-event drift may reflect delayed processing, confounding, or a risk premium.

## Instrumental variables: relevance and exclusion

An instrument \(Z\) must predict treatment \(D\) (relevance) while affecting outcome \(Y\) only through \(D\) under the design's exclusion restriction, with additional assumptions such as independence and often monotonicity for a local average treatment effect. A strong first stage does not establish exclusion. In finance, proposed instruments can directly move discount rates, liquidity, or risk, violating the very condition needed for a causal interpretation.

## Identification audit

Before estimating, state the estimand, units, treatment, comparison, timing, assignment mechanism, assumptions, interference risks, and target population. Draw a causal graph if it helps separate confounders, mediators, and colliders; controlling for a post-treatment mediator or collider can introduce bias. Report sensitivity and falsification checks, but do not portray a collection of robustness checks as proof of an untestable assumption.

Connected: [[Econometrics]] · [[Economics]] · [[Economics-to-market hypotheses]] · [[Statistical inference for trading]] · [[Research workflow]]
