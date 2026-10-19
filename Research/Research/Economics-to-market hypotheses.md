# Translating Economics into Market Hypotheses

Economic theories describe incentives, constraints, equilibrium, and adjustment. A market hypothesis requires a measurable implication with clear timing, a tradable instrument, and a method that can distinguish competing explanations.

## Translation chain

1. **Economic mechanism:** e.g. a supply constraint, inventory adjustment, policy surprise, financing constraint, or information delay.
2. **Observable proxy:** identify data that measures the mechanism, including its error and release process.
3. **Information time:** specify when each observation was public and when prices could react.
4. **Market mapping:** define instruments exposed to the mechanism, with direction and horizon.
5. **Competing explanation:** risk premium, broad factor, seasonality, liquidity, or reverse causality.
6. **Empirical design:** event study, panel/time series, cross-sectional comparison, causal design, or predictive test.
7. **Trading translation:** costs, execution, constraints, sizing, capacity, and risk.
8. **Validation:** chronological holdout, independent source/market test, robustness, and decay monitoring.

## Macro data require real-time vintages

Macroeconomic series are revised and often published after the reference period. Forecasting with final revised values can create look-ahead bias. Store release timestamps, original values, revisions, consensus expectations, and surprise definitions separately. The timestamp when a number is known is distinct from the period it describes.

## Regime dependence is testable, not a free explanation

If a proposed relationship only works in recessions, high-volatility periods, or a specific policy regime, define that condition ex ante and estimate uncertainty within it. Avoid searching thresholds after observing returns. The regime may itself be measured with future-revised data or subject to classification error.

## Example: fiscal news to rates / FX

Possible mechanism: an unexpected change in fiscal outlook shifts expected issuance, demand, inflation, or policy reaction. Candidate data include release-time budget documents, auction results, real-time forecasts, yields, inflation expectations, and exchange rates. Design must distinguish fiscal news from simultaneous economic news, global risk, central-bank expectations, and pre-announcement pricing. A yield/FX response is not automatically a profitable strategy; assess transaction costs, event timing, and cross-country variation.

## Example: physical supply data to futures

Possible mechanism: a transport bottleneck changes expected regional inventory and near-term convenience yield. Use timestamped shipping, weather, port, production, and inventory releases; map route/grade/location to contracts and calendar spreads. Test whether data arrival precedes price movement and whether it adds value over public reports, seasonality, and known inventory releases.

## Hypothesis card (worked template)

- **Mechanism:** what constraint/incentive transmits the shock?
- **Observable:** what is measured, by whom, and with what error?
- **Availability:** earliest decision-time usable version, including latency/revisions.
- **Exposure:** which instruments should respond most and which serve as placebo?
- **Prediction:** sign, horizon, conditionality, and benchmark.
- **Alternative explanations:** anticipation, shared news, risk compensation, seasonality, selection, or source artifact.
- **Falsifier:** what result would materially weaken/reject the mechanism?
- **Decision translation:** executable prices, costs, capacity, and risk mapping.

Example: if a weather shock reduces hydroelectric supply, the predicted effect may differ across power hubs depending on interconnector capacity, storage, and fuel substitution. A national rainfall average may not measure the constrained basin. The mechanism suggests geographic heterogeneity and a placebo hub; it does not establish a directional trade until forecasts, plant/infrastructure data, and market timing are aligned.

Related: [[Economics]], [[Econometrics]], [[Causal inference]], [[Time series]], [[Alternative-data research design]], [[Futures]], [[Forex]], [[Fixed Income]].
