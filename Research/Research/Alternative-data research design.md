# Designing Research with Alternative and Obscure Data

Obscure data can reveal under-measured economic activity, but the hunt itself creates severe selection and reproducibility risks. This framework preserves unusual ideas while testing them rigorously.

## Step 1: Register the lead

Record the original story, anecdote, paper, or data discovery; source grade; date; why it might matter; who could observe it; and what mechanism could connect it to a market outcome. Separate factual claims from conjecture.

## Step 2: Understand the measurement process

Map how events produce records, how a collector samples them, and when they become observable. Document coverage, revisions, backfill, platform/API changes, geographic/venue bias, missingness, selection, and licensing. A proxy often measures its own collection process as much as the target phenomenon.

## Step 3: State falsifiable predictions

Write direction, affected assets, horizon, lead/lag, expected conditionality, and a null. Specify a primary test before broad exploration. Include negative controls or placebo outcomes that the mechanism should not predict.

## Step 4: Construct a point-in-time dataset

Preserve event time and ingestion/publication time separately. Version each record and transformation. Avoid using a current database's backfilled historical history as though it had been available at the time.

## Step 5: Use staged exploration

Explore a small development sample for feasibility, then lock feature/target choices. Use chronological validation, nested tuning, an untouched test or forward paper-trading phase, and a complete ledger of all data and model variants. Consider false discovery/multiple testing if the lead came from a broad scan.

## Step 6: Seek independent confirmation

Test another source, geography, market, time period, or measurement proxy that the mechanism predicts should behave similarly. A result that exists only in one opaque vendor product could be a vendor artifact.

## Step 7: Test implementation and decay

Model publication latency, collection delay, cleaning, signal computation, trading delay, liquidity, spread, fees, borrow, and impact. Estimate what happened between first public discovery and simulated deployment; monitor degradation over time.

## Step 8: Separate discovery from confirmation

If a lead was found by searching a wide collection of data families, markets, horizons, or outcomes, the discovery sample has already informed the hypothesis. Freeze one primary prediction and evaluate it on a genuinely independent source/time period or a prospective collection. Replication should be chosen because the mechanism predicts it, not because it is the subgroup that worked. Report failed replications and changes in measurement.

## Lead scorecard (for prioritization, not truth)

Score separately: mechanism specificity; point-in-time availability; measurement/coverage auditability; legal accessibility; independent confirmation potential; expected cost/capacity; and novelty. A low evidence grade does not mean discard—it means label as a lead and design a proportionate falsification test. A high-priority lead is not thereby evidence of alpha.

## Example hypotheses (leads, not asserted edges)

For a broader inventory of candidate data families and access caveats, see [[Alternative data opportunity map]].

- Shipping/port congestion may proxy commodity supply disruptions with lags determined by route and inventory buffers.
- Weather anomalies may influence power, agricultural, or transport markets conditionally on season and local infrastructure.
- Public job postings may reveal firm investment or sector demand but have recruiter/platform coverage biases.
- Stablecoin flows or exchange funding may provide a state variable for crypto liquidity; exchange labels and internal transfers need careful treatment.
- Text frequency may measure attention rather than fundamentals; test the distinction using unrelated attention proxies and timing.

## Stop conditions

Stop or downgrade the lead when timestamp availability is impossible to reconstruct, legal data rights are unclear, the signal disappears under reasonable costs/lag, plausible alternatives explain it, or repeated search exhausts the independent evaluation sample. Keep the negative result in the log and source note.

Connected: [[Alternative data]], [[Statistical inference for trading]], [[Research workflow]], [[Edge validation]], [[Source grading]].

For proxy measurement and pre-specified negative controls, see [[Alternative-data measurement and negative controls]].
