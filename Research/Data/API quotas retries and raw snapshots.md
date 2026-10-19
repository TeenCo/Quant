# API Acquisition: Quotas, Retries, and Raw Snapshots

## Acquisition contract

Treat each request as a durable task: source/product, canonical parameters, date range, pagination cursor, attempt number, request time, response status/headers, byte count, row count, and checksum. Persist raw response bytes before parsing whenever terms allow. Normalize into a separate versioned layer. If retention is disallowed, retain permitted query metadata and document that exact replay is unavailable.

```yaml
request_id: sha256(source|endpoint|canonical_params|cursor)
retrieved_at_utc: 2026-10-18T12:00:00Z
http_status: 200
cursor_in: null
cursor_out: page-token
payload_sha256: "..." # only if permitted
complete: true
retry_after_seconds: null
```

## Retry policy

Classify `429` and documented transient `5xx`/network timeouts separately from authentication, malformed query, and permanent `4xx` errors. Honor `Retry-After`; otherwise use bounded exponential backoff with jitter, a maximum attempt/time budget, and a shared rate limiter across workers. Retry idempotent GETs; for writes, require idempotency keys or reconcile state first. Persist successful pages atomically and resume from the last committed cursor. Never convert failed/empty/error JSON into zero observations.

Apply provider-specific quotas, burst limits, daily budgets, and pagination caps. Reserve capacity for recovery. Log request IDs and redacted metadata, not keys or sensitive payloads. Detect partial pagination by checking cursor progression, expected completion signals, and coverage counts. Schedule overlapping refresh windows only when corrections are expected, and store each response as a new snapshot.

## Operational failure modes

Thundering-herd retry after outage; rate limit hidden behind HTTP 200 error body; dropped page treated as completed; duplicated page on resume; stale cache mistaken for fresh result; partial file committed; daylight-saving range boundary skipped; token leak in logs; provider changes schema without version bump.

## Falsifiable QC exercise

Use a mock endpoint that returns 429 with `Retry-After`, transient 503, repeated cursor, malformed successful JSON, then valid pages. Verify bounded request rate, exact page-once persistence, explicit failed status for malformed response, and final row count/checksum. Compare a cold full pull with interrupted/resumed pull; normalized outputs must match exactly. No licensed payload is required for this test.

## Primary references

- [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110) — **Grade 1**, IETF standards-track specification (2022), primary protocol source; establishes HTTP semantics, not provider quota policy.
- [RFC 6585: Additional HTTP Status Codes](https://www.rfc-editor.org/rfc/rfc6585) — **Grade 1**, IETF primary standard (2012), includes 429 and Retry-After behavior; does not dictate an optimal client backoff.
- [NOAA CDO API documentation](https://www.ncei.noaa.gov/cdo-web/webservices/v2) — **Grade 1**, official maintained API docs; documents source-specific limits, which may change and do not generalize to other APIs.

Connected: [[Research pipeline architecture]] · [[Performance]] · [[Financial data source directory]]
