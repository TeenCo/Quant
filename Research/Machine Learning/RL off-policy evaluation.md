# Reinforcement Learning Off-Policy Evaluation

## Core idea

Off-policy evaluation (OPE) estimates a target policy's value from trajectories collected under a behavior policy. For a trajectory, per-decision importance sampling weights are \(w_t=\prod_{j=0}^t\pi(a_j\mid s_j)/\mu(a_j\mid s_j)\), yielding a weighted reward estimate. Large or zero-support ratios cause variance or non-identification. A doubly robust estimator combines a fitted value/Q model with importance correction; it is not robust to absent action support or arbitrary simulator misspecification.

Finance example: evaluate a new limit-order aggressiveness policy using logged historical order decisions, where state includes only decision-time book data and behavior propensities are recorded.

## Leakage and validation failures

- Require overlap: actions plausible under target policy must have positive probability under logged behavior. Diagnose state-action support before reporting a point estimate.
- Estimate behavior propensities and Q/value models using cross-fitting or held-out trajectories; do not fit and evaluate on identical episodes without correction.
- Sequential weights compound; report clipping choice, effective sample size \((\sum w)^2/\sum w^2\), weight tails, and unweighted/model-based comparators.
- Historical replay misses market impact and strategic response. Policy-induced transitions differ from fixed-tape assumptions, especially for large orders.
- Reusing the same test trajectories to design reward, tune policy, and report OPE makes estimates selected. Reserve a final chronological trajectory set and report sensitivity.

## Research exercise

On a logged execution dataset with known behavior propensities, compare direct-method, per-decision importance sampling, and doubly robust estimates for a conservative policy change. Use trajectory-level chronological splits, cross-fit nuisance models, report support coverage/effective sample size and bootstrap-by-day intervals, then vary weight clipping and compare against a high-fidelity simulator. Treat disagreements as model-risk evidence, not a reason to select the favorable estimator.

## Sources (graded)

- **Grade 1** — Jiang & Li (2016), *Doubly Robust Off-policy Value Evaluation for Reinforcement Learning*, ICML. Recency: established (2016); novelty: doubly robust OPE estimator. Type: peer-reviewed conference paper. Direct: https://proceedings.mlr.press/v48/jiang16.html . Limit: estimator assumptions and benchmarks do not resolve market impact or support failures.
- **Grade 2** — Sutton & Barto (2018), *Reinforcement Learning: An Introduction*, 2nd ed., Chapter 5. Recency: standard modern text (2018); novelty: synthesis of Monte Carlo and importance-sampling foundations. Type: scholarly textbook, openly linked by authors. Direct: http://incompleteideas.net/book/the-book-2nd.html . Limit: broad RL exposition rather than finance-specific OPE validation.
