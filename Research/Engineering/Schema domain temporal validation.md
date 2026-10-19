# Schema, Domain, and Temporal Validation

Validation has three distinct questions: can the payload be parsed, does it obey declared economic invariants, and is its timing/mapping valid for the intended research use? Passing schema checks alone does not establish correctness.

## Example contract

```yaml
table: daily_bar
version: 2
key: [security_id, session_date, source_snapshot_id]
columns:
  security_id: {type: string, nullable: false}
  session_date: {type: date, nullable: false, timezone: exchange_calendar}
  available_at: {type: timestamp_tz, nullable: false}
  open: {type: decimal, unit: quote_currency/share}
  high: {type: decimal, unit: quote_currency/share}
  low: {type: decimal, unit: quote_currency/share}
  close: {type: decimal, unit: quote_currency/share}
  volume: {type: decimal, unit: shares, nullable: true}
```

Structural checks: exact required columns/types, uniqueness, null policy, parseability, response completeness. Domain checks: `low <= min(open,close) <= max(open,close) <= high`, valid session, market-aware sign/size constraints, units and currency. Temporal checks: timezone-aware timestamps, availability not earlier than publication/receipt rule, session calendar, monotonic event sequence where required, no feature timestamp later than decision cutoff. Define severity and disposition (fail/warn/quarantine); store rule version, offending keys, examples, and approved exceptions. Never silently drop anomalies.

## Failure modes

Schema drift coerces identifier to integer and strips leading zero; UTC conversion shifts session date; generic positive-price rule rejects legitimate negative futures; adjustment mismatch creates fake returns; a valid timestamp is actually bar-open rather than bar-close; missing pagination passes as a sparse-but-valid table; schema permissiveness hides unexpected columns.

## Falsifiable QC exercise

Create a fixture with valid bars plus one malformed type, duplicate key, crossed OHLC, negative-but-permitted futures price, DST boundary, stale availability timestamp, and one missing page marker. Assert expected pass/warn/quarantine per instrument convention; run the same checks after serialization round-trip. Falsification criterion: any known injected fault passes silently or a permitted negative futures observation is rejected solely by a generic rule.

## Primary references

- [Pandera documentation](https://pandera.readthedocs.io/en/stable/) — **Grade 5**, primary project docs, actively maintained; technical API guidance, but schemas encode researcher assumptions rather than economic truth.
- [Great Expectations documentation](https://docs.greatexpectations.io/docs/) — **Grade 5**, primary project docs, current product guidance; useful expectation/reporting patterns, not independent evidence of data correctness.
- [Arrow columnar format specification](https://arrow.apache.org/docs/format/Columnar.html) — **Grade 1**, Apache project technical specification, maintained; format semantics only, not a domain-validation standard.

Connected: [[Data validation patterns]] · [[Research pipeline architecture]] · [[Data provenance and point-in-time]] · [[Order book data and event-time reconstruction]]
