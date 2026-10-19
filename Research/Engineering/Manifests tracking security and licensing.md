# Manifests, Tracking, Security, and Licensing

## Run and data manifest

Make a run reconstructable without embedding credentials or restricted content. Include IDs and digests rather than secrets; capture both source access metadata and research choices.

```yaml
run_id: uuid
created_at_utc: timestamp
code_revision: git-commit-or-tree-digest
environment_lock_digest: sha256
data:
  - source_product: provider/product
    endpoint: documented-endpoint
    query_digest: sha256-canonical-redacted-query
    retrieved_at_utc: timestamp
    snapshot_id: immutable-id-or-unavailable
    content_hash: hash-if-terms-permit
    license_ref: URL-or-agreement-reference
    retention_basis: permitted | metadata-only | unknown
universe_version: id
cutoffs: availability-rule
config_digest: sha256
seed: integer-or-na
outputs: [artifact-id]
```

Tracking systems can store parameters, metrics, artifacts and run relationships; they do not by themselves establish valid splits, complete trial accounting, data rights, or trustworthy lineage. Preserve failed/null runs and define artifact access controls. Keep API keys in environment/secret manager, redact authorization headers and query tokens, use least privilege, rotate credentials, and avoid secret-bearing URLs in logs. Check raw snapshots, notebook outputs, caches, and crash dumps for accidental leakage.

## Rights and reproducibility

Record license/terms version, permitted research/commercial uses, storage/retention, derived-data and redistribution constraints, attribution, and expiry/termination duties. SDK terms do not necessarily grant rights to underlying data. If payload retention is prohibited, record only allowed request metadata and mark snapshot reproducibility unavailable; do not evade restrictions via hashes or transformed copies without confirming terms.

## Failure modes

Credential committed in manifest; private data copied to shared artifact store; license field records URL but not applicable product/agreement; moving vendor endpoint makes query irreproducible; hash itself disallowed; tracker silently overwrites run; full query includes API key; container digest omitted while dependencies drift.

## Falsifiable QC exercise

Create a synthetic manifest and scan it plus generated logs/artifacts with a secret-pattern test. Verify no credential value appears; ensure every data input resolves to source, query digest, timestamp, terms reference, and retention status. Re-run in a clean environment from pinned code/config and permitted fixtures; compare output digest or stated numeric tolerance. Falsification criterion: missing input lineage, secret detection, or unexplained output divergence.

## Primary references

- [MLflow Tracking documentation](https://mlflow.org/docs/latest/ml/tracking/) — **Grade 5**, primary project docs, maintained; describes tracking functionality, not experiment validity or secure deployment by default.
- [DVC data and pipeline versioning](https://dvc.org/doc) — **Grade 5**, primary project docs, maintained; documents workflow tooling, not a grant of rights to versioned data.
- [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) — **Grade 1**, official NIST security-control catalog (2020, updated 2022), authoritative controls; broad organizational guidance, not a specific implementation recipe.
- [U.S. Copyright Office: Fair Use Index](https://www.copyright.gov/fair-use/) — **Grade 1**, official government legal information, current index; does not determine rights for a particular dataset or replace applicable license/contract review.

Connected: [[Experiment reproducibility]] · [[Experiment tracking implementation notes]] · [[Research pipeline architecture]] · [[Data provenance and point-in-time]]
