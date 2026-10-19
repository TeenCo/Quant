# Commodities

## Instruments and structure

Commodity exposure may use futures, spot/physical contracts, ETFs, swaps, or producer equities. Seasonality, storage, transport, location/grade, delivery, and inventory create market-specific dynamics.

## Data considerations

Track contract expiry/roll, inventory publication time and revisions, delivery points, weather, shipping, production, refinery/processing constraints, seasonality, and price limits. Continuous futures require an explicit roll methodology.

Primary physical-market leads include [EIA Open Data](https://www.eia.gov/opendata/) for energy supply, inventories, flows, and prices; [CFTC COT](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm) for lagged positioning; and [NOAA NCEI](https://www.ncei.noaa.gov/cdo-web/webservices/v2) for weather/climate observations. Align each value to its actual publication/collection time and capture revisions.

For a research-design example combining vessel activity, inventories, trade, and commodity contracts, see [[Alternative data case study - physical supply chain]].

Additional source leads for satellite fire observations, crop-progress reports, port throughput, aviation and fisheries data are cataloged in [[Sources/Official satellite, transport and activity datasets]].

## Research angles

Term-structure carry, inventory/supply shocks, weather, shipping/port activity, seasonality, cross-commodity spreads, positioning, and macro/FX linkages.

## Physical balance to traded contract

Start by specifying commodity, grade, location, delivery month, and the physical constraint. A national inventory number may not measure deliverable stocks at the futures delivery point; pipeline capacity, refinery configuration, storage economics, quality differentials, and transport bottlenecks can dominate. Map the hypothesized shock to the specific contract/spread expected to respond, and predefine a control series with weaker exposure.

## Inventory release example

For a weekly inventory release, keep reference period, collection period, release timestamp, revision vintage, and consensus snapshot separate. Define the surprise as actual minus pre-release consensus, with units and seasonal adjustment stated. Test event-window changes using tradable quotes after release latency, control for simultaneous releases and market hours, and examine whether the response concentrates in relevant maturities/locations. A retrospective revised series cannot be treated as the first release unless vintages are available.

## Seasonal and storage structure

Seasonality in production/consumption means calendar-month comparisons may be more meaningful than raw levels; however, seasonal adjustment can itself use revised/full-sample estimates. Compare year-over-year and seasonal-baseline surprises only with data known at the time. Contango/backwardation reflects a mix of financing, storage, convenience yield, risk premia, and delivery options. Analyze actual contract spreads and roll policy rather than assuming a continuous price history captures the trade.

## Weather/transport leads

Forecast weather is available in successive vintages; realized weather is not a valid substitute for the forecast that traders had. Shipping/AIS coverage varies by receiver, vessel class, congestion, and gaps; route inference may be probabilistic. Measure source latency and coverage, construct negative controls (unaffected routes/grades), and seek independent confirmation in official inventory/flow data. Keep these signals as hypotheses until point-in-time and cost-aware evidence exists.

## Links

[[Futures]] · [[Alternative data]] · [[Economics]] · [[Market data]] · [[Edge validation]] · [[London Strategic Edge]]
