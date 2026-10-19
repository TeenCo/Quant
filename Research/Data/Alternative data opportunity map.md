# Alternative Data Opportunity Map

Alternative data can add observations about physical activity, attention, supply chains, institutions, and behavior. It can also add measurement bias, delayed availability, legal constraints, and many more researcher degrees of freedom. Treat every item below as a **research lead**, not a proven source of alpha.

## Lead families

| Family | Example observables | Potential market connection | Main validity risks |
|---|---|---|---|
| Energy operations | Storage, production, refinery utilization, electricity load, outages | Crude/products, gas, power, utilities, inflation-sensitive assets | Release lag, survey estimation, revisions, geography/grade mismatch, policy changes |
| Weather and climate | Temperature anomalies, precipitation, storm tracks, drought | Agriculture, power, gas, insurance, shipping | Station coverage, forecast vs realized weather, spatial aggregation, seasonality, revisions |
| Trade and customs | Imports/exports by commodity, country, port, HS/NAICS category | FX, commodities, country/sector equities, rates | Classification changes, confidentiality suppressions, monthly lag, valuation vs physical volume |
| Shipping / AIS | Vessel positions, port calls, draught, destination, ship-to-ship events | Energy, dry bulk, agriculture, freight, insurers | Satellite/receiver coverage, spoofing, identity resolution, missing transmissions, destination inference |
| Satellite / remote sensing | Night lights, crop conditions, inventories, industrial activity | Agriculture, metals, energy, regional growth | Cloud/observation gaps, processing revisions, proprietary transformations, proxy ambiguity |
| Public filings / text | SEC filings, earnings transcripts, policy releases, court/regulatory documents | Equities, credit, rates, FX, sector baskets | Publication/acceptance time, amendments, parsing quality, selection and text-model leakage |
| Consumer / digital activity | Search interest, app usage, web prices, job postings, reviews | Consumer equities, inflation, labor, retail, travel | Platform coverage, bots, sample selection, backfills, API changes, licensing/privacy |
| Policy / geopolitical events | Sanctions, trade restrictions, elections, conflict, regulation | Country exposures, FX, commodities, credit, sector/issuer spreads | Event date ambiguity, anticipation, narrative coding, concurrent news, subjective classification |
| Satellite / thermal anomalies | Fire detections, radar/optical scenes, surface properties, trace-gas products | Power, gas, refining, mining, agriculture, emissions-sensitive assets | Overpass/cloud limits, sensor/product version, model-derived interpretation, arrival latency |
| Agriculture survey and crop status | Crop progress, planting/harvest stage, condition ratings | Grain futures, calendar spreads, food processors, FX of exposed exporters | Survey aggregation, seasonal sampling, release lag, subjective ratings, revisions |
| Aviation / mobility | Aircraft state vectors, airport/carrier passenger or cargo statistics | Airlines, travel, airports, fuel, regional economic activity | Receiver coverage, aircraft filtering, commercial-use terms, aggregate release delay |
| Port operations | Container throughput, vessel/cargo counts, import/export/empty categories | Freight, retail, manufacturing, commodity flows | Port-specific categories, delayed reporting, no global coverage, seasonal closures |
| Fisheries / vessel activity | AIS/VMS-derived apparent fishing effort, vessel encounters and route activity | Seafood, fishmeal, regional food supply, maritime risk | NGO/model-derived classification, selective VMS input, AIS gaps, commercial license restrictions |
| Rail and grid operations | Railroad performance/waybill reports, regional power generation/load/outages | Industrial production, energy, metals, regional growth | Restricted or delayed products, operator-region coverage, settlement and reporting revisions |

## Evidence scale and acquisition status

- **Official source data:** EIA, NOAA NCEI, U.S. Census, SEC EDGAR, CFTC, and statistical agencies; often Grade 1–2 for what they publish, but still require timing, revisions, and construction checks.
- **Primary private/vendor feeds:** maritime AIS products and commercial alternative datasets; typically Grade 5 for vendor feature claims until coverage/completeness are independently assessed.
- **Articles, reports, stories:** good for hypothesis discovery, not proof; grade the specific claim separately.

## Source leads with reviewed documentation

- [[Financial data source directory]] covers EIA, NOAA, Census trade, SEC, CFTC, BIS, and relevant access notes.
- EIA's [Weekly Petroleum Status Report](https://www.eia.gov/petroleum/supply/weekly/) provides weekly balance, inventory, imports/exports and other tables with release materials and prior issues. EIA documentation notes tables and methodology can change; preserve report vintage and release timestamp.
- Census [Monthly International Trade](https://www.census.gov/data/developers/data-sets/international-trade.html) is available from January 2010 onward and is revised annually with April statistics. Preserve release vintages and commodity classifications.
- NOAA [Climate Data Online API](https://www.ncei.noaa.gov/cdo-web/webservices/v2) provides station and dataset metadata plus observations; an API token is required and rate limits apply.
- MarineTraffic/Kpler [data services](https://www.marinetraffic.com/en/ais-api-services) advertise live/past AIS, port events, and vessel records, with commercial access/demo inquiry. Treat coverage and predictive-event products as vendor claims; validate independently. AIS observations are not complete global vessel truth.
- [[Sources/Fisman Hamao Wang 2014]] is an academic example of testing an unusual political-exposure channel using defined events and firm-level exposure.
- [[Sources/Rolnick et al 2019]] is a broad ML/climate application map, not evidence of market return prediction.
- [[Sources/Official satellite, transport and activity datasets]] documents official satellite, crop, aviation, port and fisheries activity sources. Global Fishing Watch and OpenSky access conditions may prohibit ordinary commercial research unless additional permission is obtained.
- [[Sources/Global macro and national statistics sources]] broadens the macro universe to IMF, OECD, Eurostat, UNData, India, and Mexico.
- [[Sources/Cross-market reference prices and public market data]] expands public reference/market sources and documents why reference rates, aggregate reports, delayed displays, and executable quotes must not be conflated.

## Build a lead hypothesis before querying

Write: **mechanism → measurement → availability → exposed market → test → falsifier.** For example, a potential port disruption might affect a grade/location-specific commodity curve only after vessel congestion is observable, with a lead determined by transit and inventory buffers. Name a placebo port or unrelated contract the mechanism should not affect.

## Connected notes

[[Alternative-data research design]] · [[Economics-to-market hypotheses]] · [[Data provenance and point-in-time]] · [[Commodities]] · [[Forex]] · [[Equities]] · [[Statistical inference for trading]]
