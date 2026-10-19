# Bitemporal and Versioned Data Joins

## Model the clocks explicitly

Point-in-time data commonly needs two independent intervals: **valid time** (when a fact applies in the modeled world) and **transaction/knowledge time** (when the system knew that version). For trading research, retain source publication and local receipt separately too; availability is the earliest defensible decision-time boundary, not necessarily the source's reference date.

```sql
CREATE TABLE fact_version (
  series_id TEXT, reference_period DATE, value DOUBLE PRECISION,
  valid_from TIMESTAMPTZ, valid_to TIMESTAMPTZ,
  known_from TIMESTAMPTZ, known_to TIMESTAMPTZ,
  source_release_id TEXT, ingested_at TIMESTAMPTZ,
  PRIMARY KEY (series_id, reference_period, known_from)
);
```

Use half-open intervals `[from,to)` to avoid boundary ambiguity. For a decision timestamp `t`, a version is eligible when `known_from <= t AND t < known_to`; among eligible versions, apply the declared valid-time and aggregation policy. If the source only supplies latest corrected history, prior knowledge states cannot be recreated: label the join latest-history, not point-in-time.

```sql
SELECT d.decision_id, f.value, f.source_release_id
FROM decisions d
LEFT JOIN LATERAL (
  SELECT * FROM fact_version f
  WHERE f.series_id = d.series_id
    AND f.reference_period <= d.cutoff_period
    AND f.known_from <= d.decision_time
    AND d.decision_time < COALESCE(f.known_to, 'infinity')
  ORDER BY f.reference_period DESC, f.known_from DESC
  LIMIT 1
) f ON TRUE;
```

Do not substitute this pattern blindly for event streams: specify whether the decision uses latest observation, latest release, a fixed reference period, or a window aggregate. Preserve timezone offsets and source timestamp precision. Close the old version interval and insert a new row on correction; never overwrite history.

## Failure modes and controls

- **Look-ahead revision:** final value joined to old decision; test against a known revision example.
- **Boundary leakage:** date-only release timestamp makes a pre-release decision eligible; use full timestamp/timezone and conservative receipt time.
- **Overlapping knowledge intervals:** two versions qualify; enforce exclusion/uniqueness constraints and report overlaps.
- **Duplicate selection:** ties on publication timestamp; add deterministic source sequence/release ID tie-break.
- **Late-arriving duplicate:** ingestion timestamp mistaken for publication; retain both clocks.
- **Invalid-time semantics:** corrected value backdated as though always true; distinguish valid time from when correction became known.

## Falsifiable QC exercise

Construct a 3-period series with an initial release and one later correction. At cutoffs before release, between releases, and after correction, assert the expected version IDs and that no future-known record is selected. Inject an overlapping interval, a timezone-offset error, and a same-timestamp tie; each must fail loudly. Falsification criterion: any pre-publication decision changes when a later vintage is appended.

## Primary references

- [FRED API observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html) — **Grade 1**, current official endpoint documentation, primary service semantics, high novelty for versioned macro joins; documents real-time/vintage parameters, but not every series' release schedule or local receipt latency.
- [Temporal data management (Snodgrass, book/site)](https://www2.cs.arizona.edu/~rts/tdbbook.pdf) — **Grade 2**, foundational technical reference (1999), high conceptual novelty, primary academic text; older database context, not a finance feed specification.

Connected: [[Data provenance and point-in-time]] · [[Data vintage and real-time testing]] · [[Research pipeline architecture]]
