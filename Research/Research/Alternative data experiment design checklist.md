# Alternative-Data Experiment Design Checklist

Use this checklist before large downloads, feature sweeps, or strategy searches.

## A. Claim and mechanism

- [ ] State one economic mechanism, not only a correlation or story.
- [ ] Specify which market/instrument is exposed and why.
- [ ] Define a falsifying observation and at least one negative control/placebo.
- [ ] Record the source/evidence grade and distinguish source fact from hypothesis.

## B. Source and data rights

- [ ] Identify the data-generating process, collectors, intermediaries, and units.
- [ ] Read terms for research, commercial use, retention, internal sharing, derivatives, and redistribution.
- [ ] Record access key/account, request limits, sampling, API versions, and paid/restricted fields.
- [ ] Determine whether values are direct measurements, vendor labels, estimates, forecasts, or inferred classifications.

## C. Timing and vintage

- [ ] Preserve event/reference time separately from publication/arrival/receipt time.
- [ ] Establish whether historical data are point-in-time or retrospectively backfilled.
- [ ] Preserve revisions, release vintages, preliminary flags, and correction history where available.
- [ ] Model collection, processing, and decision latency before the simulated trade.

## D. Measurement and coverage

- [ ] Quantify geographic, venue, population, instrument, and time coverage.
- [ ] Characterize missingness, outages, reporting incentives, selection, and denominator changes.
- [ ] Validate entity and identifier mapping with effective dates.
- [ ] Compare a sample to official records or an independent provider.
- [ ] Document schema, units, classification, aggregation, and methodology breaks.

## E. Statistical design

- [ ] Specify target, horizon, primary test, baseline, and metrics in advance.
- [ ] Use chronological splits and nested search; keep final evaluation isolated.
- [ ] Record every alternative feature, threshold, region, lag, window, and outcome tried.
- [ ] Control for seasonality, common factors/news, dependence, multiple testing, and selection.
- [ ] Report effect size, uncertainty, null results, and sensitivity—not just a selected p-value.

## F. Economics and execution

- [ ] Map the data to price formation, supply/demand, risk, or participant constraints.
- [ ] Compare with existing public information and simpler proxies.
- [ ] Include instrument/venue mapping, trading calendar, spread, delay, fees, financing, borrow, impact, and capacity.
- [ ] Test whether market reaction begins before data publication (anticipation) or after feasible execution.
- [ ] Estimate decay from data release and from public discovery.

## G. Decision and reproducibility

- [ ] Classify result as lead, exploratory finding, replicated result, or unresolved.
- [ ] Store data card, code/config/version, query, data vintage, and checksum if permitted.
- [ ] Append a timestamped entry to [[log]] and link to relevant market/method notes.
- [ ] Record the next replication or invalidation test.

Related: [[Alternative-data research design]] · [[Alternative data opportunity map]] · [[Data provenance and point-in-time]] · [[Statistical inference for trading]] · [[Research workflow]]

## Go / pause decision

Proceed to broad acquisition only if the claim has a concrete market mapping, source terms permit the intended use, timing can be audited or explicitly downgraded, and the primary test plus falsifier are written. Pause when source meaning or licensing is unresolved. Reject a claimed historical-trading interpretation when the relevant availability vintage cannot be reconstructed; preserve it as exploratory evidence if useful.
