# Forecast Evaluation and Comparison

Forecasting is an operational exercise: a forecast is made at an origin using information then available, evaluated against a later realization, and compared to a relevant benchmark. In markets, ranking accuracy or low forecast error is not itself a trading edge.

## Define the forecast experiment

Specify before evaluation:

- Forecast origin and information cutoff.
- Target, horizon, units, and whether the target overlaps across origins.
- Benchmark(s): zero/mean, random walk, seasonal naive, simple factor/rule, or current production method.
- Loss function and decision use: squared error, absolute error, quantile loss, log score, directional/rank utility, or net portfolio utility.
- Evaluation window, rolling/expanding refit schedule, and handling of missing data.

All forecasts must be generated in chronological order. Model fitting, feature selection, scaling, and hyperparameter selection happen only within the data available at each origin.

## Loss and economic relevance

For forecast `f_t` and realization `y_t`, choose a loss `L(y_t, f_t)` that matches the use. Squared-error loss heavily penalizes large misses; absolute error is more robust; quantile loss evaluates conditional quantiles. For a trading decision, also evaluate an explicit net utility after turnover, spread, fees, impact, financing, and constraints.

Avoid selecting a loss metric after inspecting which one makes a model look best. Report predictive scores and decision/portfolio results separately.

## Comparing two forecasts

Let `d_t = L_A,t - L_B,t` be the loss differential. The Diebold–Mariano framework tests whether the expected differential is zero, with a variance estimate that must account for serial correlation induced by multi-step horizons or overlapping targets. Small evaluation samples, model selection, nonstationarity, and repeated testing affect inference. Use a benchmark-aware design; do not claim universal model superiority from a single p-value.

### Worked example: variance forecasts

At each origin \(t\), forecast the next horizon's realized variance \(y_t>0\), obtaining forecasts \(f_{A,t}\) and \(f_{B,t}\). A convenient illustration is squared-error loss:

\[
L(y,f)=(y-f)^2,\qquad d_t=(y_t-f_{A,t})^2-(y_t-f_{B,t})^2.
\]

If \(\bar d<0\), model A has lower average squared loss in this evaluation sample. That sign alone does not show reliable superiority: overlapping horizons make adjacent \(d_t\) dependent, and model selection can bias the observed mean. A HAC standard error can be used for the mean loss differential under an appropriate weak-dependence design; a block bootstrap is another option if blocks preserve the dependence and the complete model-selection procedure is represented.

Squared error emphasizes large misses. For positive variance targets, QLIKE is another common choice:

\[
L_{QLIKE}(y,f)=\log(f)+y/f,
\]

up to terms depending only on the realized value under a common convention. Forecasts must be strictly positive. State the exact implementation because QLIKE conventions and normalization vary. No loss is universally best: use one aligned with the statistical target, then separately measure decision value.

### Paired comparison uncertainty

For \(n\) forecast origins, let \(\bar d=n^{-1}\sum_t d_t\). A naive standard error \(s_d/\sqrt{n}\) presumes independent loss differentials. When forecasts cover an \(h\)-step overlapping horizon, neighboring outcomes share returns; even if one-step innovations are independent, the loss differentials will generally not be. Estimate long-run variance from the autocovariances of \(d_t\), or use a design-specific resampling procedure. Avoid mechanically setting the HAC lag equal to the horizon without checking frequency, overlap, and refitting structure.

If many model variants are compared, the best model's observed loss difference is selected and biased in its favor. Treat the model search as part of the experiment: use nested chronological selection, retain outer-fold predictions only, and apply multiplicity-aware interpretation to final comparisons.

## Common financial complications

- **Overlapping labels:** multi-period returns share observations and create serial dependence.
- **Refitting:** a model repeatedly estimated at each origin differs from a fixed model fitted once.
- **Regime change:** average performance can hide periods where the model fails badly.
- **Heavy tails:** squared-error scores may be driven by a few extreme observations.
- **Asymmetric decisions:** false positives and false negatives can have different costs.
- **Selection:** comparing many candidate models and reporting the winner reintroduces multiple-testing bias.
- **Trading translation:** a good conditional mean forecast can still have poor rank, calibration, or executable value.

## Practical reporting

Report loss differentials by fold and regime, an uncertainty interval, benchmark and test design, refit cadence, calibration, tail behavior, gross/net trading utility, and the complete candidate model search. Keep the final holdout isolated from tuning. See [[Statistical inference for trading]] and [[Data vintage and real-time testing]].

### Forecast-to-decision bridge

A forecast is useful only if it changes a decision in a way that improves expected utility. Let action \(a\) produce utility \(U(a,y)\), and let \(\mathcal{I}_t\) denote information available at origin \(t\). The ideal action is

\[
a_t^*=\arg\max_{a\in\mathcal{A}}\mathbb{E}[U(a,Y_{t+h})\mid\mathcal{I}_t].
\]

Lower forecast loss does not guarantee a better action if forecast differences occur where the action is unchanged, are poorly calibrated in decision-critical tails, or are smaller than costs. A robust report therefore gives both (i) predictive loss/calibration and (ii) a pre-specified decision rule's net utility, with costs and constraints measured at implementable times.

For example, a volatility forecast may improve QLIKE yet produce no portfolio improvement if leverage is already capped. Conversely, a small forecast gain in a tail-risk region could be valuable if the decision is a risk limit. Explain this mapping instead of treating forecast metrics as alpha.

## Sources and connected notes

- [[Sources/Diebold Mariano 1995]] — test of equal predictive accuracy, with serial correlation treatment as a core concern.
- [[Sources/Forecasting Principles and Practice]] — free online introduction to forecasting workflows and evaluation.
- [[Time series]] · [[Structural breaks and parameter instability]] · [[Volatility models]] · [[Edge validation]] · [[ML validation]]
