# Official Satellite, Transport and Activity Datasets

Scope: additional physical-world source families beyond the vault's established EIA, NOAA, Census trade, SEC, and commercial maritime AIS leads. These are source and measurement notes, not evidence of investable alpha.

- **Reviewed:** 2026-10-18. Verified by opening primary publisher documentation/pages linked below; exact operational limits and licenses should be rechecked at acquisition.
- **Evidence grade:** 1 for publisher statements about its own data/access and methods; 5 for vendor/NGO derived activity claims pending independent validation. Grade is claim-specific.
- **Recency:** current publisher pages reviewed 2026-10-18, except where version/product period is explicitly stated.
- **Novelty:** Medium as a focused collection of official physical activity sources; source datasets themselves range from established to current.
- **Type:** government / intergovernmental primary data, NGO-derived model outputs, and selected community/provider feeds.

## Source families

### NASA FIRMS — active fire and thermal anomalies

- **Measured variable:** MODIS/VIIRS satellite thermal-anomaly / active-fire detections, with observation time and geolocation; this is a detected hotspot, not a direct measure of burned area, fuel consumed, or facility output.
- **Access/auth:** Web maps, downloads (SHP/KML/TXT), web services; global API access uses a MAP_KEY. Review the service documentation before automation.
- **Granularity/timing:** Individual detections at sensor footprint scale; global near-real-time products are distributed within about 3 hours of satellite observation (US/Canada real-time per NASA page). Multiple satellite overpasses create uneven temporal sampling.
- **Revisions/coverage/permission:** NRT feeds and archived science-quality products are distinct; NRT records can be replaced/updated. Cloud, smoke, overpass timing, fire size/intensity, and sensor thresholds affect detection. NASA data use/citation/disclaimer apply; verify product-specific terms.
- **Grade 1; recency current; novelty medium; type official satellite observations/product processing.**
- **Primary URLs:** [FIRMS home and delivery overview](https://firms.modaps.eosdis.nasa.gov/) · [Active fire data](https://firms.modaps.eosdis.nasa.gov/active_fire/) · [Web services](https://firms.modaps.eosdis.nasa.gov/web-services/) · [NASA Earthdata FIRMS background](https://www.earthdata.nasa.gov/data/tools/firms)
- **Limitations:** detections can be missed or duplicated; thermal anomaly does not identify cause; do not interpret missing detections as no activity.

### Copernicus Sentinel and Climate Data Store

- **Sentinel measured variables:** Sentinel-1 radar backscatter (day/night, cloud-penetrating imaging); Sentinel-2 optical reflectance and spectral bands; Sentinel-3 ocean/land color and surface-temperature products; Sentinel-5P atmospheric trace-gas/aerosol products. Raw/reprocessed level and derived products differ substantially.
- **Access/auth:** Copernicus Data Space Ecosystem catalog/download/API (OData, STAC, S3, openEO). Registration/authentication is used for platform access; account does not imply unrestricted compute or redistribution. CDS has a catalogue and API; dataset access is open/free per C3S overview, with applicable dataset terms.
- **Granularity/timing:** Sentinel-1/2 scenes are spatially resolved at product-dependent pixel sizes (commonly 10 m for selected bands/products); revisit is constellation/orbit and latitude dependent, not a guaranteed daily panel. CDS includes station/in-situ observations, reanalyses, climate records, seasonal forecasts and projections, with dataset-specific grids, time steps, and release delays.
- **Revisions/coverage/permission:** CDSE products have processing baselines and reprocessing/version changes; CDS dataset licenses and metadata specify product-specific coverage and updates. Record collection ID, processing baseline, acquisition time, publication/availability time, and download time. Clouds limit optical imagery; radar has geometry/speckle effects. Do not confuse forecast/reanalysis with contemporaneously available observations.
- **Grade 1; recency current; novelty medium; type intergovernmental EO products and climate datasets.**
- **Primary URLs:** [CDSE documentation](https://documentation.dataspace.copernicus.eu/) · [Sentinel mission catalog docs](https://documentation.dataspace.copernicus.eu/Data.html) · [CDSE authentication/API overview](https://documentation.dataspace.copernicus.eu/APIs.html) · [C3S Climate Data Store overview](https://climate.copernicus.eu/climate-data-store) · [CDS catalogue/API portal](https://cds.climate.copernicus.eu/)
- **Limitations:** converting imagery/reanalysis into mine, stockpile, crop, or industrial-activity estimates requires a separately validated measurement model. Spatial resolution is not temporal timeliness.

### USDA NASS — Crop Progress and Condition / Quick Stats

- **Measured variable:** surveyed, state-level percent planted/progress at crop phenological stages and subjective crop-condition categories (including good/excellent); NASS publishes corresponding crop estimates and other agricultural survey statistics.
- **Access/auth:** weekly report PDFs and web products via NASS/ESMIS; Quick Stats database/API requires an API key. NASS also publishes downloadable data files.
- **Granularity/timing:** crop, state, reference week ending Sunday; National Crop Progress reports generally publish weekly during the growing season (release calendar governs actual date/time). Not a field-level sensor.
- **Revisions/coverage/permission:** report calendars, corrections, methodology/quality notes, and historical series should be retained. Availability and crops/states vary by season and program. Public government statistics; obey site/API terms and cite NASS. The reference week is not the information timestamp.
- **Grade 1; recency current; novelty low-medium; type official survey statistics.**
- **Primary URLs:** [NASS Crop Progress and Condition](https://www.nass.usda.gov/Charts_and_Maps/Crop_Progress_&_Condition/) · [NASS publications and reports calendar](https://www.nass.usda.gov/Publications/) · [Quick Stats](https://quickstats.nass.usda.gov/) · [Quick Stats API documentation](https://quickstats.nass.usda.gov/api)
- **Limitations:** survey sampling/subjective ratings, state aggregation, seasonal coverage, and scheduled publication lag; imagery/vegetation indices are not equivalent measures.

### Global Fishing Watch (GFW) — apparent fishing effort and vessel products (NGO-derived)

- **Measured/derived variables:** GFW combines publicly available AIS with partner-provided vessel monitoring system data and applies models to estimate apparent fishing effort, encounters, identity, and other activity. These are NGO-produced derived datasets, not an official government census and not raw complete global vessel truth.
- **Access/auth:** API token required; GFW documentation explicitly says APIs are available **only for non-commercial purposes**. Commercial trading use is not licensed by public API access; obtain written permission or exclude. Bulk export is documented.
- **Granularity/timing:** spatial/time-cell or event/vessel-level depending on endpoint/product; product release dates and historical coverage differ. Check endpoint-specific docs and data timestamps.
- **Revisions/coverage/permission:** model versions, input AIS coverage and partner VMS availability can create retrospective changes. Store product/version, query and retrieval snapshots; do not treat a current API response as historical point-in-time. Attribution/license and non-commercial restriction apply.
- **Grade 5 for derived activity feature claims; recency current; novelty medium; type NGO-derived, mixed input sources.**
- **Primary URLs:** [GFW API documentation](https://globalfishingwatch.org/our-apis/documentation/) · [API license and rate limits](https://globalfishingwatch.org/our-apis/documentation/docs/license-rate-limits) · [GFW data portal](https://globalfishingwatch.org/data/)
- **Limitations:** non-commercial restriction is dispositive for ordinary commercial investment research; algorithmic inference, AIS gaps/spoofing, selective VMS partnerships, and model revisions impair point-in-time interpretation.

### Aviation: FAA statistics and OpenSky (different data rights)

- **FAA measured variables:** published operational/performance, airport, airline, passenger/cargo and aviation statistics; selected products are aggregate and reported at airport/carrier/time-period levels. Availability and cadence vary by linked dataset.
- **Access:** FAA pages link to data downloads and DOT/BTS TranStats; largely public web downloads. Check dataset-specific terms and release calendars.
- **OpenSky measured variables:** ADS-B/Mode-S-derived state vectors (aircraft identity/callsign where available, position, velocity, heading, altitude and timestamps). The API documents second-level state updates, reusing a position for at most 15 seconds and dropping stale state vectors.
- **OpenSky access/permission:** API authentication/access rules apply. Official API documentation describes research/non-commercial use; its terms say commercial live-flight retrieval requires contacting OpenSky. Do not presume commercial use is permitted.
- **Granularity/timing/coverage:** OpenSky state vectors are near-real-time and geographically dependent on receiver coverage, aircraft transponder behavior and filtering. FAA aggregates are generally slower and can be monthly/annual. Coverage varies for blocked/limited aircraft and regions.
- **Revisions:** FAA statistical tables may be corrected/updated; OpenSky live snapshots are not automatically an immutable historical archive. Preserve retrievals; historical datasets/access have separate terms.
- **Grade 1 FAA source claims; Grade 2 OpenSky data structure/access; recency current; novelty low-medium; types official statistics / community research network.**
- **Primary URLs:** [FAA Aviation Data & Statistics](https://www.faa.gov/data_research/aviation_data_statistics) · [FAA data downloads](https://www.faa.gov/data_research/aviation_data_statistics/data_downloads/) · [OpenSky API docs](https://opensky-network.github.io/opensky-api/) · [OpenSky terms](https://opensky-network.org/about/terms-of-use)
- **Limitations:** FAA aggregates are not flight-by-flight real-time activity; ADS-B sightings are not a complete schedule/manifest or passenger count. OpenSky commercial restrictions require resolution before use.

### Port authority operational statistics — Port of Los Angeles example

- **Measured variable:** monthly/yearly container throughput with imports, exports and empties; separate cruise/passenger, automobile, breakbulk and liquid-bulk statistics. Current operations page links to vessel/cargo tools.
- **Access/auth:** public website/downloads; Port states statistics are free of charge and requests credit. No general bulk API established by reviewed source.
- **Granularity/timing:** port-level monthly/yearly tables by cargo category. Monthly release is not necessarily real time; capture first-publication/receipt timestamps.
- **Revisions/coverage/permission:** preserve downloaded table/version; page does not establish a formal revision policy. Port-specific rather than global; categories and units differ across ports. Credit publisher and check linked terms.
- **Grade 1 for published port series; recency current; novelty medium; type port authority operational statistics.**
- **Primary URLs:** [Port of Los Angeles statistics hub](https://www.portoflosangeles.org/business/statistics) · [Container statistics](https://www.portoflosangeles.org/business/statistics/container-statistics) · [Cargo operations](https://www.portoflosangeles.org/business/operations)
- **Limitations:** throughput records are lagged, port-specific and often aggregate container counts rather than commodity weights/values; not an independent global congestion measure.

### Rail and grid: scoped leads, not promoted as established source records here

- **Rail:** U.S. STB collects railroad performance and waybill information, but public reporting differs by series and some operational detail is restricted. Start at [STB data and statistics](https://www.stb.gov/reports-data/). Verify dataset, public release cadence, definitions and permitted use before forming a feature; no single uniform public real-time rail movement feed verified in this pass.
- **Grid:** EIA remains the principal documented official US electricity generation/load/outage dataset in the existing source note. Grid operator feeds (e.g., [PJM data miner](https://dataminer2.pjm.com/)) expose market/operational fields with product-specific account/API terms and regional coverage; verify field cadence, historical retention, settlement revisions, and license before use. Operator telemetry is not interchangeable with national EIA statistics.
- **Grade 2 for the existence of publisher portals; recency current; novelty low-medium; type official/regional operator data.** Kept as leads because field-level access/terms/cadence were not sufficiently checked to grade their series claims.

## Falsifiable research hypotheses — **LEAD ONLY; no evidence of alpha**

1. **Fire and power/gas:** For pre-registered thermal anomaly clusters inside a fixed buffer of power, gas, or refining assets, higher newly observed fire counts should predict a measurable next-session change in nearby regional power/gas basis or outage announcements relative to matched unaffected regions. Use only FIRMS observations whose NASA observation and first-retrieval timestamps precede the trade cutoff; test event-time and weekly panels, seasonal/weather controls, cloud/overpass exposure, and matched placebo assets. **Falsifier:** no incremental out-of-sample effect versus weather/outage controls, or effect disappears after latency and transaction costs.
2. **Crop progress surprise:** State-crop progress lag versus its own seasonal history, measured only from the timestamped NASS release, should relate to subsequent grain futures returns/spreads when the release surprise is large and crop exposure is high. Freeze the pre-release expectation using only then-available data; compare exposed crop contracts with unrelated grains and non-release weeks. **Falsifier:** no robust conditional response after release-time alignment, weather controls, historical revisions and costs.
3. **Sentinel facility activity:** At a pre-registered set of industrial/mining sites, cloud-screened/radar-observed activity proxy changes may forecast monthly output/commodity-basis changes. Use only scenes publicly available by each historical decision time; hold out sites and years; calibrate proxy against reported outcomes. **Falsifier:** no incremental accuracy over published production/seasonality or results depend on retrospective reprocessing unavailable then.
4. **Aviation activity:** FAA airport/carrier statistics may offer slow confirmation of travel demand; do not use OpenSky commercial API unless written permissions allow the intended use. Test whether first-published traffic surprises forecast later airline/airport earnings revisions relative to consensus, retaining release vintages and controlling for seasonality/capacity. **Falsifier:** no out-of-sample incremental forecast value beyond disclosed schedules, fuel, macro and earnings information.
5. **Port throughput:** Monthly LA container import/export/empty counts may predict short-horizon freight/retail-sensitive outcomes only around timestamped surprises. Compare with Census trade releases and other ports; model release-day availability, seasonal closures and subsequent revisions. **Falsifier:** no incremental contribution after Census data, calendar effects and realistic execution costs.
6. **Fishing activity (permission-gated):** GFW apparent fishing-effort anomalies might map to fishmeal/seafood supply exposure, but **commercial hypothesis testing is blocked absent explicit commercial rights**. If authorized, compare model-version snapshots with independent landings/trade data and unaffected regions. **Falsifier:** no independent confirmation, or result is driven by changing AIS/VMS coverage.

For all designs, preserve raw payloads, source version, reference/observation time, first publication/arrival time, retrieval time, permissions, and transformations. Separate measured data from modeled features; prevent look-ahead via vintage-aware joins and use chronological, selection-aware validation.

## Related vault notes

[[Data/Alternative data opportunity map]] · [[Sources/Official alternative-data sources]] · [[Data/Data provenance and point-in-time]] · [[Research/Data vintage and real-time testing]] · [[Research/Point-in-time feature availability contract]] · [[Research/Alternative-data research design]] · [[Research/Alternative data experiment design checklist]] · [[Research/Alternative data case study - physical supply chain]] · [[Markets/Commodities/Commodities]]
