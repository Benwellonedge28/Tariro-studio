# Durable redacted record

**ZIP-AUDIT-RECORD-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/record.rs`

## Boundary and inputs

AuditDraft becomes an immutable AuditRecord only after validation and [redaction](redaction.md). For the candidate v1 hash body, encode the compact ASCII JSON array of these ordered fields: edition string with exact value 1, workspace UUID, sequence decimal string, audit identity UUID, actor principal UUID or null, actor category tag, operation kind tag, operation reference UUID, reviewed operation digest or null, decision reference UUID or null, policy digest or null, scope digest or null, revocation epoch decimal string or null, outcome tag, evidence digest or null, canonical UTC timestamp. Use lowercase canonical UUID strings and Foundation tagged digests and timestamps. Actor tags are human, service, agent and unattributed. Outcome tags are denied, pending, confirmed, failed and unresolved. Operation kinds must use registered ASCII tags. Emit quoted ASCII fields and unquoted null with commas and brackets and no whitespace. Require attribution and decision fields for privileged records.

## Behavior and failure handling

Store predecessor and computed digest separately from the canonical body. Reject undeclared fields, malformed tags or absent mandatory attribution before hashing. Encode evidence collections as a qualified immutable reference when needed. No raw names, credentials, commands, environments or private paths may appear in the body. Preserve the declared codec edition and reject unqualified future encodings before writes.

## Acceptance

**ZIP-AUDIT-RECORD-T01.** Construct equivalent typed inputs in different orders and compare exact bytes and digest. Add an undeclared field or missing privileged attribution and verify rejection before journal mutation. Inspect staged bytes for synthetic secret canaries.
