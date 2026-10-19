# Macro Mechanism to Market Data and Vintages

## Mechanism-to-observable chain

Write primitive shock \(\rightarrow\) affected agent/constraint \(\rightarrow\) observable macro measure \(\rightarrow\) cash-flow, expectations, discount-rate, or risk-bearing channel \(\rightarrow\) named market outcome and horizon. For each macro observation retain reference period, first-publication timestamp/value, revision vintage, and local receipt/usable time. A feature at decision time \(t\) must use the vintage actually available by \(t\), not latest revised history.

## Worked example: CPI surprise and front-end rates

Hypothesis: an upside CPI surprise raises short-maturity yields through an expected policy-path revision. Map reference month, official release time, first print, pre-release timestamped consensus, surprise (first print minus consensus), target OIS/futures contract, and executable event window. Separate the surprise from revisions; note market hours and overlapping releases. This is a testable hypothesis, not an established return effect.

## Assumptions and failure modes

- An indicator is a proxy, not the mechanism; definitions, seasonal adjustment, and benchmark revisions alter history.
- Latest-vintage data create look-ahead when revisions were unavailable to the historical decision.
- Consensus requires timestamp, coverage, and staleness checks.
- Event returns are not automatically causal: anticipation, leakage, simultaneous news, liquidity, and risk-premium repricing confound.
- ALFRED/FRED vintage dates do not prove when an individual vendor delivered usable data.

## Falsifiable exercise

For 100 scheduled CPI releases, reconstruct first prints, pre-release consensus snapshots, timestamps, and one-minute front-end futures prices. Test signed surprise against a fixed five-minute yield change, comparing point-in-time and latest-vintage reconstruction. Falsify the directional implication if the coefficient is nonpositive under the prespecified interval or disappears after excluding revisions/stale consensus.

## Claim-specific sources

- FRED API exposes observation retrieval and series vintage-date endpoints; FRED and ALFRED provide distinct documented interfaces: grade **1/10** for API behavior; recency **official documentation accessed 2026-10-18**; novelty **low**; source type **official technical documentation**; [FRED API documentation](https://fred.stlouisfed.org/docs/api/fred/). Page directly checked. Limit: no guarantee of vendor receipt timestamp, trading usability, or predictive value.
- CPI-to-rate transmission here: grade **4/10 as a hypothesis, not an empirical claim**; recency **not applicable**; novelty **context-specific**; source type **proposed mechanism and falsification design**. No single empirical source is used to assert the example effect.

Related: [[Economics]] · [[Econometrics]] · [[Causal inference]] · [[Data vintage and real-time testing]] · [[Forecast evaluation]]
