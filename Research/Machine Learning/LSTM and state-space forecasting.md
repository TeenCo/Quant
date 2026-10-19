# LSTM and State-Space Forecasting

## Core idea

An LSTM updates memory via \(c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t\), with learned gates controlling retention and writing. A linear state-space model writes \(z_t=Fz_{t-1}+w_t\), \(y_t=Hz_t+v_t\); the Kalman filter propagates a state distribution using a specified transition/observation model. LSTM memory is learned and nonlinear; state-space structure makes latent dynamics explicit and can yield interpretable uncertainty under assumptions.

Example: forecast intraday volatility from returns and order-flow summaries using an LSTM and a stochastic-volatility/state-space baseline, then compare forecast calibration and risk sizing.

## Leakage and validation failures

- Sequence inputs must end at the actual decision availability time; target windows begin afterward. Purge overlapping target intervals and avoid random window-level splits.
- Fit normalization per training fold; global sequence normalization leaks future moments.
- Hidden-state resets, warm-up periods, and retraining cadence must match deployment. Carrying state across a split can leak validation observations into training context.
- Longer lookback and more gates do not establish economically stable memory; compare against lag features, persistence, AR, and explicit state-space baselines.
- State-space filtering is online; smoothing uses future observations and is retrospective only.

## Research exercise

Forecast next-day realized variance with (a) HAR-style lag regression, (b) small LSTM, and (c) a local-level/state-space model. Use nested walk-forward windows, fold-local scaling, explicit sequence warm-up, and purging. Compare QLIKE, interval coverage, calibration by volatility state, and risk-managed net utility; include latency and refit cadence.

## Sources (graded)

- **Grade 1** — Hochreiter & Schmidhuber (1997), *Long Short-Term Memory*, Neural Computation. Recency: foundational (1997); novelty: gated memory architecture. Type: peer-reviewed primary methods paper. Direct: https://doi.org/10.1162/neco.1997.9.8.1735 . Limit: original tasks do not show modern financial generalization.
- **Grade 2** — Durbin & Koopman (2012), *Time Series Analysis by State Space Methods*, 2nd ed. Recency: standard text (2012); novelty: systematic inference reference. Type: scholarly book. Direct: https://global.oup.com/academic/product/time-series-analysis-by-state-space-methods-9780199641178 . Limit: book access may be restricted; link only, and particular model assumptions must be checked.
