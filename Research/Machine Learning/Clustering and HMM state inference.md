# Clustering and HMM State Inference

## Core idea

K-means partitions points by minimizing \(\sum_i\|x_i-\mu_{z_i}\|^2\); it ignores temporal order. A hidden Markov model instead posits latent state \(z_t\), transition matrix \(A_{jk}=P(z_t=k\mid z_{t-1}=j)\), and emission model \(p(x_t\mid z_t)\). The filtered posterior \(P(z_t\mid x_{1:t})\) is updated recursively; the smoothed posterior \(P(z_t\mid x_{1:T})\) uses future observations and is not deployable at time \(t<T\).

Example: infer high/low volatility-liquidity conditions from lagged realized volatility, spreads, and volume; use filtered state probabilities as portfolio risk controls, not as labels for a discovered economic truth.

## Leakage and validation failures

- Full-sample centroids/scalers, HMM smoothing, or retrospectively relabeled states leak future distribution/state information.
- Fit on the training window and use filtering online; at each refit log parameter availability and state-label mapping (state indices can permute).
- Choose state count and features in inner chronological validation, not by best outer-period strategy return.
- Gaussian emissions can be fragile under heavy tails; crisis observations may dominate scaling/fit. Compare robust/simple state rules and assess posterior uncertainty.
- Cluster stability is not predictive validity; assess whether state-conditioned decisions improve net out-of-sample utility beyond lagged volatility baselines.

## Research exercise

Fit 2–4 state Gaussian HMMs to daily lagged realized volatility and spread measures. Compare one-step filtered probabilities to a lagged-volatility threshold through walk-forward refits. Measure state persistence, posterior entropy, transition stability, and net utility of a predeclared risk-scaling rule; contrast against a smoothed-state retrospective chart to quantify look-ahead optimism.

## Sources (graded)

- **Grade 1** — Rabiner (1989), *A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition*, Proceedings of the IEEE. Recency: classic (1989); novelty: comprehensive algorithmic exposition. Type: peer-reviewed tutorial. Direct: https://doi.org/10.1109/5.18626 . Limit: speech examples; state models require careful financial specification.
- **Grade 2** — Hamilton (1989), *A New Approach to the Economic Analysis of Nonstationary Time Series and the Business Cycle*, Econometrica. Recency: foundational (1989); novelty: regime-switching macro time series. Type: peer-reviewed primary paper. Direct: https://doi.org/10.2307/1912559 . Limit: macro model application, not proof of tradable market regimes.
