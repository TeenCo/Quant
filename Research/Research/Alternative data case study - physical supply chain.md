# Case Study: Physical Supply-Chain Signals as Tradable Hypotheses

This is a research-design example, not a claimed profitable strategy.

## Hypothesis skeleton

**Mechanism:** A disruption or congestion event delays physical commodity flows, shifting expected nearby availability, regional basis, or calendar spreads.

**Observation candidates:** Vessel AIS positions/calls/draught; port queues; EIA inventory/flow releases; Census import/export values and quantities; weather; futures curves; related freight rates.

**Exposed instruments:** Choose contracts matching the commodity grade, location, delivery window, and physical route. A broad front-month proxy may be poorly aligned with the physical mechanism.

## Test design

1. Select a commodity-route pair and pre-register the event definition (e.g., port-call duration exceeding a seasonal threshold).
2. Build the event using only records received by each historical timestamp; retain raw AIS messages/provider snapshots and the observation vintage.
3. Construct a mechanism-based exposure map: cargo/ship class, origin, destination, cargo capacity, route alternatives, inventory buffer, and relevant contract delivery point.
4. Specify outcomes before looking: nearby calendar spread, regional basis if available, or market response within fixed post-observation horizons.
5. Use control routes/ports, unaffected commodities, and placebo dates; compare to inventories, official releases, futures curve, and weather as baselines.
6. Account for public release calendars, vessel reception gaps, inference delays, forecasted ETAs, futures roll, bid/ask, and market impact.
7. Validate on later periods, different routes, or independent official trade/inventory sources.

## Failure modes to explicitly investigate

- AIS dark periods or receiver coverage shifts coincide with perceived congestion.
- Destination/cargo classification is inferred retrospectively or changed after arrival.
- Vessel movement reflects weather, port scheduling, sanctions, or rerouting rather than commodity shortage.
- Official data are monthly/weekly and revised; using reference dates instead of release dates leaks information.
- Event threshold is chosen after searching many ports, periods, vessel classes, and outcome windows.
- Market already prices expected disruption before it becomes visible in the chosen dataset.
- Signal is statistically detectable but too small/slow to overcome spread, impact, or crowded trading.

## Evidence and source handling

Official EIA and Census documentation support the identity and publication structure of their own reports. Commercial AIS coverage and historical backfills require contract/terms review and independent validation. Store source grades, data-access permissions, and revision policy in [[Data dictionary and provenance card]].

## Related notes

[[Alternative data opportunity map]] · [[Alternative-data research design]] · [[Execution costs and market impact]] · [[Commodities]] · [[Statistical inference for trading]] · [[Research exercises]]
