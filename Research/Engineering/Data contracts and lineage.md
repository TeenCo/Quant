# Data Contracts and Lineage

## Contract at every boundary

A contract specifies producer, consumer, schema/version, key, ordering, timestamp meaning, availability rule, units/currency, null policy, invariants, coverage expectation, and failure disposition. Version contract changes explicitly; do not silently reinterpret an existing column. Use backward-compatible additions where possible and reject ambiguous breaking changes.

```yaml
contract: validated_trade/v1
producer: normalize_trades
consumer: feature_builder
primary_key: [venue, instrument_id, event_id]
time:
  event_time: exchange event timestamp
  received_at: collector receipt timestamp
  ordering: [event_time, sequence_number]
units: {price: quote_currency_per_unit, size: base_units}
nulls: {sequence_number: forbidden, condition_code: allowed}
invariants: [unique(primary_key), size >= 0, received_at >= event_time_minus_clock_tolerance]
on_failure: quarantine_and_block_downstream
```

Lineage is a directed graph from source snapshot/version through parse, normalization, entity mapping, filtering, features, labels, model and report. Every node records code digest, parameters, environment, input IDs, output IDs, and validation result. A feature's lineage must resolve to raw source versions and cutoff logic. For non-retainable data, store compliant metadata/checksum only if permitted and explicitly mark reduced reproducibility.

## Failure modes

Contract drift is hidden by permissive parser; downstream output loses source IDs; mutable upstream table changes old run; lineage records code but omits query/universe version; branch-specific cleaning creates undocumented selection; retention policy causes prohibited raw data to leak into artifacts.

## Falsifiable QC exercise

Build a three-stage toy pipeline and produce a feature. Change one raw input version, one unit conversion, and one mapping table version in turn. The derived artifact ID/lineage must change and identify the exact upstream cause. Break a required field and assert downstream computation is blocked with a quarantine record. Falsification criterion: two materially different inputs resolve to indistinguishable lineage or a failed contract still yields a published feature.

## Primary references

- [W3C PROV Overview](https://www.w3.org/TR/prov-overview/) — **Grade 1**, W3C primary provenance model overview (2013), foundational/novel vocabulary for entities, activities, agents; generic provenance model, not a finance-specific contract.
- [OpenLineage specification](https://openlineage.io/docs/spec/) — **Grade 5**, primary project specification/docs, actively maintained; useful run/job/dataset event model, adoption and completeness depend on implementation.
- [Data Contract Specification](https://github.com/datacontract/datacontract-specification) — **Grade 5**, primary open-source specification repository, versioned technical project; evolving standard and not a guarantee of semantic validity.

Connected: [[Research pipeline architecture]] · [[Experiment reproducibility]] · [[Data validation patterns]] · [[Data provenance and point-in-time]]
