# FX carry and forward parity

Parent: [[Forex]]. Companion: [[Fixed Income]].

## Quote convention and parity

Let spot \(S_{A/B}\) be units of B per A; a rise means A strengthens. For simple annual money-market rates and year fraction \(\tau\), covered interest parity without basis is

\[
F_{A/B}=S_{A/B}\frac{1+r_B\tau}{1+r_A\tau}.
\]

With continuously compounded rates this is \(F=S\exp[(r_B-r_A)\tau]\). Define forward points as \(F-S\) in the pair's quoted units (brokers may scale displayed points). A long A funded in B earns, before costs, approximate B return \((S_1/S_0)(1+r_A\tau)/(1+r_B\tau)-1\); distinguish this from spot-only return. Market basis, collateral, credit, capital and tenor conventions cause deviations from textbook parity.

## Worked example

USD/JPY = 150 JPY/USD, USD rate 5%, JPY rate 1%, 3-month simple tenor \(\tau=.25\). Then fair forward \(150(1.0025)/(1.0125)=148.52\) JPY/USD, about -1.48 JPY (148 points if one point is .01 JPY). A long USD forward is not a free yield: the discount is the rate differential. A carry portfolio holding USD funded in JPY must include actual rollover/forward execution and spot path.

## Fields and clock

Store pair and base/quote, bid/ask spot and outright forward (not just midpoint points), venue/dealer, value date, tenor/date calendars, holiday adjustments, timestamp and timezone, rate source/tenor/day-count/compounding, collateral currency, NDF fixing and settlement if applicable, swap points, rollover time, fees, and quote receipt time. OTC reference rates are not executable quotes. Use point-in-time rates and calendars; account for New York close, DST, broken dates, and Wednesday/holiday multi-day rolls.

## Failure modes

Sign inversion from pair convention; compare mismatched value dates; infer carry from central-bank policy rates instead of tradable funding; omit cross-currency basis, bid/ask, collateral, margin and roll charges; treat an NDF as deliverable; apply today’s calendars or rates historically; confuse annualized differential with realized return. Triangular checks require synchronized executable sides.

## Falsifiable exercise

For a fixed liquid pair and tenor, compute CIP-implied forward from matched contemporaneous executable spot and deposit/OIS inputs, then compare executable forward bid/ask residuals. Freeze timestamp matching and calendars in advance. Test whether residuals exceed combined spreads persistently out of sample; reject apparent violations that disappear under matched value dates or costs. This is a parity diagnostic, not an alpha claim.

## Source leads

- BIS, *Triennial Central Bank Survey* (2022; primary survey, grade 2; reputable, broad coverage, less novel; FX market structure and turnover, not parity proof): https://www.bis.org/statistics/rpfx22.htm .
- BIS Quarterly Review, *The failure of covered interest parity: FX hedging demand and costly balance sheets* (2016; institutional empirical analysis, grade 2; older but directly relevant; evidence is period- and currency-specific, not a universal causal decomposition): https://www.bis.org/publ/qtrpdf/r_qt1609e.htm .
- ECB euro reference rates (official daily reference, grade 4 for valuation context; current page, low novelty; explicitly not a transaction price): https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html .
