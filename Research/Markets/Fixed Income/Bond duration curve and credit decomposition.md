# Bond duration, curve risk and credit decomposition

Parent: [[Fixed Income]]. Related: [[Futures]], [[Time series]].

## Sensitivity and curve exposures

Modified duration \(D_{mod}=-(1/P)(\partial P/\partial y)\); convexity \(C=(1/P)(\partial^2P/\partial y^2)\). For small parallel yield change \(\Delta y\), \(\Delta P/P\approx-D_{mod}\Delta y+\tfrac12C(\Delta y)^2\). Use decimal yields (25bp = .0025). For nonparallel moves use key-rate durations \(KRD_i=-(1/P)\partial P/\partial y_i\); approximate return \(-\sum_i KRD_i\Delta y_i\), with convexity and spread components added as needed. Credit spread duration is not Treasury duration.

## Worked example

Price 100, modified duration 6, convexity 40, yield rises 25bp. Approximation: \(-6(.0025)+.5(40)(.0025)^2=-.014875\), or -1.4875 points. This is a local estimate assuming stated yield convention/cashflows; option exercise, curve twist, spread and liquidity can change the result.

## Fields and clock

Identifier, coupon, maturity, day count, frequency, clean/dirty price, accrued interest, settlement date, call/put/sinking features, curve inputs and timestamps, benchmark/zero/par/swap curve type, compounding, quote side/size, evaluated vs trade flag, rating and effective time, spread definition, TRACE execution/publication time, default/recovery and corporate events. Preserve curve construction inputs, not only derived yield.

## Failure modes

Mix clean and dirty prices; use bp as decimal; treat parallel duration as total risk; compare spread measures with different curves; use stale evaluated marks as executable; infer default probability directly from yield spread; omit callability, taxes, liquidity and recovery; forward-fill sparse bond marks and understate risk.

## Falsifiable exercise

For a chosen liquid bond universe, calculate ex-ante duration/KRD from disclosed cashflows and test whether realized price changes over fixed windows reconcile with curve moves and spread changes. Compare evaluated marks with timestamped transactions where available; predefine stale-quote exclusion and report residual distributions. This is a risk-model diagnostic, not alpha.

## Source leads

- US Treasury daily par yield curve data (official; grade 1 for its published series, current; par curve is not a zero curve or intraday executable quote): https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve .
- FINRA TRACE fixed income data (regulatory trade reporting; grade 2 for reported transaction scope, current program; access products, delays and dissemination constraints apply): https://www.finra.org/finra-data/fixed-income .
- FINRA bond information (investor education; grade 3, maintained, low novelty; generic and not a valuation model): https://www.finra.org/investors/investing/investment-products/bonds .
