# Audit-safe data reduction

**ZIP-AUDIT-REDACTION-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/redaction.rs`

## Boundary and inputs

Reduce an input to the registry-approved typed fields for its operation and disclosure policy before canonical encoding or persistence. Omit raw environments, command text, prompts, credentials, private path text and opaque adapter error strings. Use scoped identifiers and eligible validated evidence digests only. Never create a digest of a secret for a public or redacted record.

## Behavior and failure handling

Apply a separate query or export projection when disclosure requires additional redaction. Do not modify an existing chained record to produce that view. An unsafe optional field is omitted; a required field that cannot be represented safely blocks the append. Bound diagnostics and never include rejected raw bytes. Redaction proof carries policy revision and source category.

## Acceptance

**ZIP-AUDIT-REDACTION-T01.** Include synthetic token, private path and malicious diagnostic in the draft. Verify all remain absent from persisted bytes, projected views and error logs. Inject a required unredactable field and verify the privileged append fails closed.
