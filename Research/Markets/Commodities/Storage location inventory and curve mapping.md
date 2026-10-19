# Commodity storage, location and inventory mapping

Parent: [[Commodities]]. Related: [[Futures]], [[Alternative data case study - physical supply chain]].

## Curve mechanics and scope

For a storable commodity, a stylized cost-of-carry relation is \(F_{t,T}=S_t e^{(r+u-y)(T-t)}\), where r is financing, u storage/insurance cost and y convenience yield. It is a benchmark, not a universal law: quality, location, transport, capacity, delivery options and market constraints matter. Define calendar spread sign explicitly, e.g. deferred minus nearby. A reported inventory total may not equal deliverable stocks at the contract's delivery point.

## Example

If spot is 80, annual financing 4%, storage 2%, convenience yield 1%, and maturity .5 years, stylized fair forward is \(80e^{(.04+.02-.01)(.5)}=82.02\). Actual futures at 85 may reflect constrained storage/location, risk premia or differing grade—not a certain 2.98 overpricing.

## Fields and clock

Commodity/grade, delivery location and month, contract specs, nearby/deferred bid/ask, inventory amount/unit and facility/geography, observation/reference period, survey cutoff, release/publication/receipt timestamps, revision vintage, seasonal adjustment, capacity/utilization, flows/imports/exports, weather forecast vintage, pipeline/port/transport constraints and currency. Link physical series to contract exposure using explicit geography/grade crosswalk.

## Failure modes

Map national inventory directly to local deliverability; mix working and total stocks or units; use revised values before release; ignore seasonality and storage capacity; infer convenience yield from curve alone; use realized weather instead of forecast vintage; assume paper contract delivery/location equivalence.

## Falsifiable exercise

Select one commodity, delivery region and official weekly inventory series. Define surprise versus a point-in-time consensus and the specific calendar spread exposed before examining outcomes. Test event-window spread changes after release latency against an unrelated maturity/grade control, using original vintages and executable spreads. Publish null results and sensitivity to revisions; no alpha assertion.

## Source leads

- EIA Weekly Petroleum Status Report schedule and data (official; grade 1 for reported US petroleum series, current weekly; national scope and revisions/definitions do not guarantee local deliverability): https://www.eia.gov/petroleum/supply/weekly/ .
- EIA Open Data API (official technical source; grade 1, current; series-specific cadence, revisions and terms must be checked): https://www.eia.gov/opendata/ .
- CME WTI contract specifications (official exchange; grade 1 for delivery/product rules, current; WTI-specific, not transferable to other commodities): https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.contractSpecs.html .
