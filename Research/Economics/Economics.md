# Economics for Quantitative Research

Economics provides theories of incentives, scarcity, institutions, production, trade, monetary conditions, and market equilibrium. It is useful for proposing mechanisms and mapping data to behavioral/economic quantities; observed association alone does not identify a mechanism.

## Major areas

- Microeconomics: preferences, constraints, competition, market design, information, strategic behavior.
- Macroeconomics: output, inflation, labor, interest rates, monetary/fiscal policy, business cycles.
- International economics: exchange rates, trade, capital flows, external balances.
- Industrial organization: market power, pricing, entry, network effects.
- Behavioral economics: limits to arbitrage and patterns in decisions.
- Financial economics: asset pricing, corporate finance, intermediary constraints, risk premia.

## Empirical bridge

Translate a proposed mechanism into measurable variables and timing. Consider reverse causality, confounders, equilibrium responses, anticipation, and policy/data revisions. [[Econometrics]] and [[Causal inference]] supply identification and robustness tools; [[Edge validation]] checks whether an empirical pattern is tradable.

## Unconventional indicators

Economic activity can sometimes be proxied by shipping, energy, weather, search, text, labor, or other data. Evaluate the data-generating process and release time in [[Alternative data]].

## Mechanism-to-observable derivation

Use a chain rather than a narrative leap:

1. **Economic shock:** specify the primitive change (e.g., supply disruption, policy surprise, demand shortfall).
2. **Constraint/incentive:** identify who changes behavior, and why substitution, inventories, contracts, or policy do not fully absorb it.
3. **Observable:** choose a measure that records the mechanism with known coverage, units, and publication time.
4. **Transmission:** map the change through costs, quantities, expectations, discount rates, or risk-bearing capacity to a market variable.
5. **Horizon and sign:** state when the market could learn the information and the expected direction/conditionality.
6. **Null and alternatives:** include a no-effect prediction and alternatives such as common news, anticipated changes, reverse causality, seasonality, or a proxy measuring reporting activity rather than economics.

Example (hypothesis only): a persistent fall in deliverable inventory may tighten a nearby commodity's physical balance. A test should specify which grade/location and contract month, how inventory release time is aligned, whether the market anticipated the release, and whether nearby-vs-deferred spreads respond more than a matched control. The mechanism does not imply a guaranteed return; storage, transport, substitution, and risk premia can offset it.

For a point-in-time macro release-to-market chain with explicit vintage clocks and a CPI-surprise example, see [[Macro mechanism to market data and vintages]].

## Equilibrium and anticipation

Observed price changes are equilibrium outcomes: supply and demand, expectations, constraints, and policy respond jointly. A public statistic can be informative about fundamentals but have little event return if traders anticipated it. Conversely, the surprise component may matter more than the level. Distinguish data release, information surprise, subsequent revisions, and actual economic reference period. For causal claims, define a counterfactual and identification assumptions; for forecasts, ask only whether the information improves a point-in-time prediction.

Connected: [[Econometrics]] · [[Causal inference]] · [[Economics-to-market hypotheses]] · [[Alternative-data research design]] · [[Edge validation]]
