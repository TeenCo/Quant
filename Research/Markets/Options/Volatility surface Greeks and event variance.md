# Volatility surface, Greeks and event variance

Parent: [[Options]]. Related: [[Implied volatility, variance risk premium and VIX]], [[Equities]].

## Surface conventions

Implied volatility is the model parameter that prices a contract given spot/forward, strike, expiry, discounting and exercise/settlement conventions. Compare surfaces by forward moneyness \(k=\ln(K/F)\) and maturity, not raw strike alone. For a European option, delta/vega conventions depend on model and quote convention; record whether IV is annualized and whether vega is per 1.00 volatility or per 1 volatility point. Greeks are local sensitivities, not invariant facts.

## Event variance decomposition

In a simplified total-variance model, \(w(T)=\sigma(T)^2T\). If event variance v_E is additive and the event lies inside expiry T1 but not T2, then \(v_E\approx w(T1)-T1\,\sigma_{base}^2\), with baseline inferred from the non-event part/adjacent maturity under stated interpolation assumptions. For expiries T1<T2 both bracketing the same single event, the difference \(w(T2)-w(T1)\) estimates intervening non-event variance only if term structure is appropriately modeled. Do not equate an IV jump to pure event variance.

## Example

An expiry 30 days away has IV 40%, total variance in year units \(.4^2(30/365)=.01315\). If a 25-day non-event baseline is 25%, its variance is \(.25^2(25/365)=.00428\); naive implied event variance is .00887, equivalent event-only annualized sigma over remaining 5 days \(\sqrt{.00887/(5/365)}=80.4\%\). This is an assumption-heavy decomposition, not a forecast guarantee.

## Fields and clock

Option identifier, right/style/settlement, strike, expiry and last trade, bid/ask/size/trade, underlying synchronized bid/ask, forward/dividend/borrow/rate inputs, quote timestamp and receipt time, IV model/version, delta convention, event announcement time and calendar vintage, corporate actions, open interest and market session. Filter crossed/stale quotes with predeclared rules; preserve raw chain and surface-fit residuals.

## Failure modes

Fit to midpoints of stale/wide markets; interpolate across event expiry without accounting for event; compare spot moneyness across dividends/rates; mix American and European models; misread vega units; annualize short-dated variance inconsistently; ignore jumps, skew, discrete hedging and bid/ask; use revised event calendar retrospectively.

## Falsifiable exercise

For one scheduled event, freeze the calendar vintage, select two expiries and a forward-moneyness grid, then calculate event variance under at least two baseline/interpolation methods using synchronized quotes. Compare implied event move distribution with subsequent realized event-window moves using a later untouched sample. Include spreads and report calibration error; no claim of tradable edge without strategy-level execution tests.

## Source leads

- Cboe Options Institute, volatility resources (exchange education; grade 3 for definitions, current collection, moderate novelty; not independent empirical evidence): https://www.cboe.com/optionsinstitute/ .
- Cboe VIX index methodology (primary index methodology; grade 1 for VIX calculation, methodology version must be checked; VIX is SPX option-implied variance measure, not single-name event IV): https://www.cboe.com/tradable_products/vix/ .
- OCC Options Disclosure Document (official clearing corporation; grade 1 for standardized option mechanics, current editions; does not specify each broker's execution/Greek model): https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document .
