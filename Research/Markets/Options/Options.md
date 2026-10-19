# Options

## Instruments and structure

Options are nonlinear claims parameterized by underlying, strike, expiry, call/put, style, settlement, multiplier, and exercise rules. Quotes may be wide or stale; implied volatility and Greeks are model-dependent.

## Data considerations

Preserve contract identifiers, quote/trade time, bid/ask, size, underlying price, dividends, rates, borrow, corporate actions, exercise/settlement, and vendor Greek methodology. Avoid survivorship in chains and use point-in-time universe/quotes. Historical prints and bars have different limitations.

## Research angles

Volatility risk premia, skew/term structure, order flow, event volatility, hedging demand, dispersion, put-call relationships, and execution/liquidity.

## Payoff and Greeks as local sensitivities

For a small change in underlying, volatility, time, and rates, a model-based option value change is locally approximated by

\[
\Delta V\approx \Delta\,\Delta S+\tfrac12\Gamma(\Delta S)^2+\text{Vega}\,\Delta\sigma+\Theta\,\Delta t+\text{Rho}\,\Delta r.
\]

These Greeks depend on the pricing model, input conventions, and point in the surface. The approximation omits higher-order terms and jumps and can fail badly near expiry or during large moves. Delta-hedged option P&L is not a pure volatility bet: gamma, realized path, discrete hedging, skew dynamics, rates/dividends, and transaction costs all contribute.

## Put-call parity as a data diagnostic

For European options with matched strike/expiry on a non-dividend asset, idealized parity is \(C-P=S-Ke^{-rT}\); with known dividends, use the prepaid forward. Large apparent violations can indicate asynchronous quotes, incorrect contract/adjustment mapping, dividend/rate error, stale markets, or genuine frictions. Do not interpret a midpoint parity residual as arbitrage without executable simultaneous prices, borrow/funding, exercise and settlement rules, and legging risk.

## Event volatility design

An earnings/event option study must separate total implied volatility from event variance and non-event baseline. Use expiries bracketing the event where possible, point-in-time event calendars, consistent surface interpolation, and matched post-event realized movement. Event inclusion, announcement timing, and revisions to event calendars can leak. The implied event component is model-dependent; compare different decomposition assumptions and maintain event-history vintages.

For a deeper treatment of implied versus realized variance, VIX interpretation, and a forecast-to-strategy research design, see [[Implied volatility, variance risk premium and VIX]]. Practice the separation between forecast evidence and executable option P&L in [[Options volatility exercise]]. Primary product/data references are graded in [[Sources/Cboe VIX methodology and data]].

[[Sources/Cross-market reference prices and public market data]] adds OCC clearing statistics/reference-data access context and contrasts aggregate reports with option quote/trade histories.

## Links

[[Equities]] · [[Probability]] · [[Market microstructure]] · [[Execution costs and market impact]] · [[Edge validation]] · [[Market data]] · [[London Strategic Edge]]
