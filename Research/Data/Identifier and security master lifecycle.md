# Identifier and Security-Master Lifecycle

## Separate entities, instruments, listings, and symbols

Ticker is a time-varying label, not a durable primary key. Model issuer/entity, security/instrument, listing/venue, and observed symbol as distinct objects. Preserve provider-native identifiers and dated mapping evidence; one issuer can have many securities/listings and one security can change symbol or venue.

```text
entity(entity_id, legal_name, lei, valid_from, valid_to)
security(security_id, entity_id, isin, share_class, currency, valid_from, valid_to)
listing(listing_id, security_id, mic, local_symbol, valid_from, valid_to)
id_alias(namespace, alias, target_id, valid_from, valid_to, known_from, known_to, source)
corporate_action(action_id, type, effective_at, announced_at, from_id, to_id, ratio, status)
```

Identifiers such as ISIN may change across corporate actions; vendor IDs may be proprietary and licensing-limited. Store identifier namespace, issuer/source, temporal validity, observation/knowledge dates, and evidence. Resolve a historical symbol using both the market date and what mapping was known at the simulated decision date. Keep delisted, bankrupt, acquired, and inactive instruments in historical universes.

## Lifecycle events to represent

Listing/IPO, symbol/name change, exchange transfer, share-class conversion, merger, spin-off, split, ADR ratio change, suspension, delisting, bankruptcy, and identifier reuse. Corporate actions are not all one-to-one mappings; represent conversion ratios and effective dates rather than simply replacing IDs. Keep raw prices and adjustment factors/version separately.

## Failure modes

- Current ticker backfilled across predecessor entities creates false history.
- Survivorship from resolving only currently active securities.
- Many-to-many mapping silently duplicates returns or fundamentals.
- Merger mapping collapses distinct securities before the effective date.
- Exchange symbol reuse maps an old event to a new issuer.
- Vendor crosswalk revisions erase what was known then.

## Falsifiable QC exercise

Build a miniature history with a ticker change, reused ticker, 2:1 split, merger, and delisting. Resolve daily observations at both event date and historical knowledge cutoff. Assert one security/listing per expected row, explicit action factor, and retention of delisted entity. Falsification criterion: changing the present-day alias table changes historical membership or maps pre-effective-date records to a successor.

## Primary references

- [GLEIF LEI search and API](https://www.gleif.org/en/lei-data/gleif-api) — **Grade 1**, official global identifier foundation docs, maintained; primary for LEI structure/relationships, not a security-level master or guarantee of market coverage.
- [OpenFIGI API documentation](https://www.openfigi.com/api/documentation) — **Grade 5**, official provider technical documentation, current service behavior, useful mapping lead; mapping quality/coverage and use rights must be tested and confirmed, and provider documentation is not independent validation.
- [SEC submissions API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) — **Grade 1**, regulator primary source, official endpoint docs; identifies filers and filings, not a complete point-in-time securities master.

Connected: [[Survivorship, identifiers and universe]] · [[Data provenance and point-in-time]] · [[Data dictionary and provenance card]]
