# Regime Stability and Forecast Comparison Exercise

This exercise examines whether a forecast adds stable information beyond simple baselines. It is educational and does not assert a profitable strategy.

## Question

Does one forecasting model consistently improve on a naive baseline across chronological test windows, and does any apparent gain depend on a particular volatility/regime period?

## Design

1. Select one liquid instrument/series and a point-in-time-safe target (e.g. next-period return or realized volatility).
2. Choose one simple benchmark and one candidate model before reviewing final results.
3. Use rolling-origin evaluation; define training window, refit cadence, horizon, and any label-overlap handling.
4. Score with a loss appropriate to the target. For returns, separate forecast loss from portfolio/decision utility; for variance forecasts, consider QLIKE and calibration.
5. Store each forecast, origin time, data vintage, model fit window, and realization.
6. Plot the loss differential and calibration over time; summarize by pre-defined volatility regimes or calendar subperiods.
7. If comparing models formally, use inference appropriate to serial correlation and overlapping horizons; do not treat each forecast origin as iid.
8. Record all model variants and avoid using the final evaluation window to tune the specification.

## Questions to answer

- Is average improvement concentrated in one episode or regime?
- How large is the uncertainty interval around the loss difference?
- Are model wins robust to an economically equivalent loss and alternative baseline?
- Does any forecast advantage improve net decision utility after realistic costs?
- Is the regime label available in real time, or defined using future/full-sample information?
- What was the total search space, including targets, horizons, models, windows, and scoring rules?

## Write-up

Include pre-specified design, data source and vintage, forecast origins, baselines, loss definition, dependence handling, per-window results, calibration, costs if translated to a trade, and limitations. Append a timestamped entry to [[log]].

## Interpretation rubric

- **Forecast improvement:** lower pre-specified out-of-sample loss with uncertainty interval and adequate calibration.
- **Stability:** gains are not explained by one episode; regime definitions are real-time-available and predeclared.
- **Economic relevance:** forecast changes a defined action and net utility after costs/constraints improves.
- **Evidence status:** exploratory if choices were informed by evaluation outcomes; confirmatory only if the design was isolated or prospectively locked.

A mixed/null result is a valid outcome. Report when performance worsens, when the forecast is less calibrated, and when simple baselines are competitive.

Related: [[Forecast evaluation]] · [[Structural breaks and parameter instability]] · [[Volatility models]] · [[Statistical inference for trading]] · [[Research workflow]]
