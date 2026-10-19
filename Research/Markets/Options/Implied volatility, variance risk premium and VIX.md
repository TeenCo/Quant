# Implied Volatility, Variance Risk Premium, and VIX

This note links option prices to risk-neutral variance, realized variance, volatility risk premia, and the practical limitations of VIX-based research. These are related quantities, not interchangeable forecasts or directly tradable assets.

## 1. From option prices to implied volatility

For a European option, a pricing model maps inputs (underlying or forward, strike, expiry, rates, distributions, and volatility) to a theoretical price. **Implied volatility (IV)** reverses that mapping: it is the volatility input that makes the model price equal an observed option price.

IV is therefore a quote expressed through a model convention, not an observed physical volatility. Results depend on the quote used, exercise and settlement conventions, rates, dividend/borrow assumptions, timestamp alignment, and model. A single IV does not summarize an option surface: compare contracts at matched expiries and moneyness/delta, and preserve skew and term structure.

### Quote and surface hygiene

- Prefer synchronized, executable bid/ask observations and retain the underlying quote; a midpoint is a mark, not guaranteed execution.
- Reject or flag crossed, locked, stale, zero-size, and implausible quotes using explicit rules. Preserve the raw record and the exclusion reason.
- Avoid mechanically inverting prices deep in the tails, near expiry, or with wide markets; inversion can amplify tiny quote errors.
- Specify forward construction and time-to-expiry conventions. Equity options require attention to dividends, borrow, early exercise, and corporate actions.
- Compare surfaces at fixed forward log-moneyness or delta, not raw strike alone, and control for changing composition of listed contracts.

## 2. Risk-neutral variance and the variance risk premium

Option prices across strikes can be combined to infer a **risk-neutral** distribution, denoted \(Q\), whereas realized returns are outcomes under the physical distribution \(P\). Under ideal assumptions and a continuum of strikes, a strip of out-of-the-money options is related to a risk-neutral expectation of integrated variance. The practical estimator uses a finite set of quotes, so truncation, bid/ask noise, jumps, rates, and discretization matter.

A useful conceptual quantity is:

\[
\text{VRP}_t(h) = \mathbb{E}^{Q}_t[RV_{t,t+h}] - \mathbb{E}^{P}_t[RV_{t,t+h}],
\]

where both expectations refer to the same horizon and variance definition. Empirically, the second term is not observed at time \(t\); a backtest often substitutes later realized variance, which creates a noisy proxy and requires careful horizon matching. **Implied variance minus subsequent realized variance is not a risk-free spread or automatic trading profit.** It can reflect compensation for bearing bad-state risk, jump risk, hedging demand, constraints, and estimation error. Selling options adds nonlinear tail exposure, path-dependent hedging costs, funding/margin requirements, and execution costs.

Distinguish:

- **Variance risk premium:** a difference between risk-neutral and physical expected variance.
- **Volatility risk premium:** terminology often used for a related premium, but definitions vary (variance vs volatility, option-implied vs model forecast).
- **Implied-realized spread:** an ex-post measurement comparing a stated implied metric with a realized metric; specify annualization, horizon, and estimator.
- **Option strategy P&L:** realized returns on an actual position including entry/exit quotes, hedge policy, fees, margin/funding, and tail losses.

## 3. What VIX does and does not say

Cboe describes VIX as a constant 30-day measure derived from a broad strip of SPX option bid/ask quotes, interpolated across eligible expiries. It is an index, not an investable asset. VIX futures and options are separate contracts with their own prices, expiries, settlement procedures, and basis to spot VIX.

Do not treat VIX as:

- A direct forecast of the next 30 calendar days' realized volatility under the physical measure.
- A tradable spot instrument that can be bought or shorted at the index value.
- A directional forecast for the S&P 500.
- A strategy signal whose performance follows from its long-run relationship with realized volatility.

Use VIX as a market-implied risk measure with a specific methodology and source timestamp. When evaluating VIX futures, model the futures contract and roll explicitly; when evaluating options on futures, use the futures underlying and correct settlement convention. The spot index, VIX futures, VIX options, SPX options, and volatility-linked ETPs should not be substituted for one another.

## 4. Worked variance-unit conversion

Suppose a 30-day annualized implied volatility is 20% and a matched-horizon annualized realized volatility is 16%. Their **volatility-point difference** is 4 points. If the target is a variance comparison, square consistently: \(0.20^2 - 0.16^2 = 0.0144\) annualized variance units. This numerical difference is not P&L. It ignores the distribution of variance, jump/tail exposure, option prices/strikes, hedging, and trading costs. Never compare an implied-volatility level to realized variance without converting units and matching horizon/annualization.

## 5. Research template: forecast comparison before strategy P&L

### Question

Does a specified option-implied variance measure improve forecasts of subsequent realized variance over a point-in-time historical baseline, and does any forecast improvement survive a tradable implementation?

### Design

1. **Fix the estimand.** Choose one underlying/index, horizon, variance definition, sampling/calendar convention, and primary forecast loss before testing.
2. **Construct information-time features.** Save option observation timestamp, quote age, bid/ask, underlying/forward, rate/dividend inputs, strike coverage, expiry selection, and calculation version. Use only records available at the forecast origin.
3. **Create matched outcomes.** Compute future realized variance over the exact target horizon. State treatment of overnight periods, jumps, holidays, and missing observations.
4. **Set baselines.** Compare to simple rolling/EWMA variance and, if relevant, a lagged realized-volatility forecast. Report a naive unconditional benchmark as well.
5. **Use chronological evaluation.** Estimate or tune only on earlier data; use rolling or expanding forecast origins. Preserve a final untouched period or conduct a prospective evaluation.
6. **Compare forecasts.** Report calibration, forecast loss (for example QLIKE where appropriate), loss differentials, and dependence-aware uncertainty. Overlapping horizons induce serial dependence; use an inference design that accounts for it.
7. **Only then simulate a strategy.** Specify exact contracts, entry and exit, hedging frequency, quote-side fills, fees, margin/funding, roll rules, and risk limits. Include stress scenarios and tail-risk summaries.
8. **Record all trials.** Log every horizon, estimator, option filter, expiry-selection rule, and subgroup tested. Adjust interpretation for selection and multiple testing.

### Invalidation checks

- The result disappears when using bid/ask-aware option marks or modest quote delay.
- It depends on a narrow strike region, stale quotes, or forward/rate assumptions.
- The forecast comparison loses significance under dependence-aware inference or in later periods.
- Apparent P&L is explained by short crash insurance, leverage, equity beta, or a few tail dates.
- A trading result depends on midpoint fills or frictionless/daily hedging that could not be implemented.

## 6. Data leads and access boundaries

- [Cboe VIX overview](https://www.cboe.com/tradable-products/vix/): current product links, descriptions, and educational material. Exchange descriptions are primary for methodology/product facts; strategy descriptions are not independent evidence that a strategy earns alpha.
- [Cboe VIX historical data](https://www.cboe.com/tradable-products/vix/vix-historical-data): page links daily OHLC CSV history from 1990 onward and legacy VXO files. The page states data are provided for convenience and accuracy is not guaranteed. Daily index history alone is insufficient to reconstruct intraday option surfaces, VIX futures returns, or executable P&L.
- [Cboe VIX term structure](https://www.cboe.com/tradable-products/vix/term-structure/): describes its SPX-option-derived term structure and point-in-time lookup. The page states updates occur approximately every 15 seconds during trading, gives availability windows, and disclaims accuracy. Confirm historical access, licensing, and timestamp semantics before use.
- [Cboe VIX FAQs](https://www.cboe.com/tradable-products/vix/faqs/) and [contract specifications](https://www.cboe.com/tradable-products/vix/vix-options/specifications/): useful for settlement, hours, and product mechanics; re-check current specifications before modeling.
- [Cboe DataShop](https://datashop.cboe.com/): commercial historical market-data channel; inspect product-specific coverage, fields, cost, terms, and redistribution permissions. No purchase or download is implied here.

For options-chain research, daily VIX OHLC is not a substitute for historical option quotes/trades, contract reference data, synchronized underlying prices, and rates/distributions. Document licenses and permitted uses using [[Data provenance and point-in-time]] and [[Financial data source directory]].

## 7. Suggested research exercise

Build a forecast-only comparison using publicly documented daily volatility history and a clearly specified realized-variance proxy. First list what can and cannot be learned from the available fields. Then design the richer version requiring historical SPX option surfaces. Compare at least one historical/EWMA baseline and one implied measure, use strictly chronological evaluation, and explain why the exercise does **not** establish a VIX trading strategy.

Questions:

1. How much does forecast ranking change with realized-variance sampling and overnight treatment?
2. Does forecast value remain after controlling for lagged realized variance and volatility regime?
3. How does uncertainty change when forecast horizons overlap?
4. What additional data are necessary to convert a forecast result into credible option-strategy P&L?

Related: [[Options]] · [[Volatility models]] · [[Forecast evaluation]] · [[Structural breaks and parameter instability]] · [[Statistical inference for trading]] · [[Execution costs and market impact]] · [[Edge validation]] · [[Data provenance and point-in-time]]
