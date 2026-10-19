# Options Volatility Exercise: Forecasts, Risk Premia, and Tradability

This exercise separates three tasks that are often conflated: describing option-implied quantities, forecasting subsequent realized variance, and testing an executable option strategy. It is a research-design exercise, not evidence of a profitable trade.

## Learning goals

- Distinguish implied volatility, risk-neutral variance, physical expected variance, and realized variance.
- Match horizons, units, and timestamps.
- Use a forecast benchmark and chronological evaluation.
- Identify the additional data needed to estimate strategy returns.

## Part A — Define the target and information set

Before viewing test results, write down:

1. The underlying and sample period.
2. A forecast origin (for example, each close) and the exact information cutoff.
3. A fixed target horizon and realized-variance estimator, including overnight returns, holidays, and jumps.
4. The option-implied feature available at that origin and its construction inputs.
5. A primary forecast loss, at least one simple benchmark, and the chronological evaluation design.

Keep the forecast output in **variance units**. If comparing volatility levels, explicitly square or take square roots as appropriate and do not mix annualization conventions.

## Part B — Audit data sufficiency

Start with the Cboe daily VIX history linked in [[Sources/Cboe VIX methodology and data]]. Inventory its fields and answer:

- Which historical forecast origins can be formed?
- Is the data daily or intraday? Does it contain contracts, strikes, or bid/ask quotes?
- Does it supply matched realized variance? If not, what separate underlying data are needed?
- Can it recreate VIX futures P&L, options P&L, or an intraday signal? Explain why not.
- What source timestamp, update history, accuracy disclaimer, and data license need to be recorded?

If suitable point-in-time realized-variance data are not available, stop at a documented data audit or obtain a source whose use is permitted. Do not invent a proxy and label it as a matched forecast test.

## Part C — Forecast comparison (when matched data are available)

Compare a single pre-specified implied-variance forecast with:

- A rolling historical-variance forecast.
- An EWMA forecast.
- A lagged realized-variance or unconditional benchmark, where appropriate.

Use rolling or expanding evaluation with all parameter selection confined to past data. Report loss by forecast origin, calibration, aggregate score, and uncertainty for paired loss differences. If horizons overlap, account for serial dependence in the loss sequence. Break results down by broad volatility regimes only as a declared secondary analysis; avoid selecting the best regime after inspecting results.

## Part D — Strategy translation boundary

Forecast superiority does not show that an option trade is profitable. To proceed to a separate strategy study, specify:

- Exact option/futures contracts and point-in-time contract universe.
- Entry and exit timestamps and fill assumptions using bid/ask or an explicitly modeled execution process.
- Delta-hedging instrument, frequency, latency, slippage, fees, and residual gamma/vega exposure.
- Dividends, rates, borrow, early exercise, settlement, margin/funding, and roll conventions.
- Drawdown and tail-risk measures, including stress periods and gap risk.
- Capacity/participation constraints and a prospective or untouched validation period.

If the paper result requires midpoint fills, idealized continuous hedging, or omits crash exposure, treat it as a model artifact until disproven.

## Deliverable

Write a one-page research memo with (a) estimand, (b) data audit, (c) pre-specified forecast design, (d) baseline and uncertainty method, (e) limitations, and (f) explicit statements of what the analysis cannot establish. Keep all attempted variants in the trial ledger.

Related: [[Markets/Options/Implied volatility, variance risk premium and VIX]] · [[Volatility models]] · [[Forecast evaluation]] · [[Regime-stability and forecast comparison exercise]] · [[Data provenance and point-in-time]] · [[Overfitting controls]] · [[Edge validation]]
