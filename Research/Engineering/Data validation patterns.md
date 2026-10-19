# Data Validation Patterns for Quant Research

Validation should catch both syntax/schema errors and economic-semantic errors. A table may parse successfully while having wrong units, timestamps, identifiers, or point-in-time meaning.

## Layer 1: Structural checks

- Expected columns and types; nullable/non-null rules.
- Unique key or documented duplicate policy.
- Parseable, timezone-aware time fields.
- Nonempty response, acceptable source status, and expected pagination completion.
- Expected coverage and plausible row counts for the requested range.

## Layer 2: Domain invariants

- OHLC bars: `low <= min(open, close) <= max(open, close) <= high`; price and volume sign conventions valid.
- Quotes: bid/ask ordering with explicit policy for locked/crossed states; sizes nonnegative.
- Returns: reconcile against prices after corporate actions and correct time alignment.
- Fundamentals: units, reporting period, filing accession, and availability timestamp coherent.
- Futures: contract code, expiry, multiplier, delivery month, and roll mapping consistent.
- Options: underlying, strike, expiry, call/put, multiplier, quote quality, and Greeks/model version recorded.
- Macro data: units, seasonal adjustment, reference period, release/vintage, and preliminary/final status captured.

## Layer 3: Temporal and cross-source checks

- Monotone event/sequence order and duplicate/out-of-order message counts.
- Expected market sessions, holiday calendars, daylight-saving shifts, and outages.
- Cross-check sampled records against a second source, official release, or raw filing.
- Detect likely stale prices and impossible jumps without automatically deleting them.
- Compare current and previous source vintages; quantify changed rows and values.

## Data-quality report

Store counts and examples for each check, version of validation rules, disposition (pass/warn/quarantine), operator or run ID, and any manually approved exceptions. Avoid silently coercing bad values or “fixing” anomalies based on expected returns.

Pandera is one Python library for declaring dataframe schemas and checks. Schema tools enforce coded rules; the research team remains responsible for choosing valid rules and data semantics.

## Severity and quarantine policy

Classify checks as hard failures (e.g., malformed schema, sequence gap that invalidates book state), warnings (e.g., unusual but plausible return), or informational diagnostics (e.g., source update count). A warning should not automatically drop observations. Store raw input, rule/version, row key, observed value, and disposition. Exceptions should be explicit and reviewable; never define an “invalid” threshold by whether the row hurts strategy performance.

## Cross-source reconciliation example

For a sample of liquid contracts, align venue, contract code, timestamp, price type, and units before comparing values. Estimate difference distributions and investigate systematic offsets, session mismatches, stale marks, and corporate/roll adjustments. Agreement does not prove either source is correct; it only bounds certain discrepancies. For official macro values, compare release/vintage and seasonal-adjustment status rather than only matching reference dates.

## Monitoring drift in data itself

Track coverage, missingness, duplicate rate, quote age, latency, symbol counts, unit distributions, schema/version changes, and cross-source residuals by time. A sudden feature distribution shift may be an economic regime change or a collection pipeline change; join diagnostics to provider notices and source metadata before attributing it to markets.

Connected: [[Data provenance and point-in-time]] · [[Market data]] · [[Research pipeline architecture]] · [[Order book data and event-time reconstruction]] · [[Schema domain temporal validation]] · [[Data contracts and lineage]]
