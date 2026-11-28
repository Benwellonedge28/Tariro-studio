# Decision audit binding

**ZIP-AUDIT-AUTHORIZATION-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/authorization.rs`

## Boundary and inputs

Bind the record to the verified decision identity, policy digest, grant scope digest, relevant revocation epoch and exact operation intent. For a denial, use the stable reason code and safe provenance permitted by scope. Audit records the observation of authorization. It does not determine or renew authorization.

## Behavior and failure handling

Verify decision, actor, workspace and operation bindings before serialization. Reject mismatched scope or unsupported mandatory policy edition. Keep attempt, decision and cleanup evidence separately attributable. Later policy or grant changes do not rewrite prior observations. Preserve no credential bytes, approval secret, or executable capability.

## Acceptance

**ZIP-AUDIT-AUTHORIZATION-T01.** Evaluate identical input under two approved policy revisions. Confirm the recorded digests differ and each record links to its own decision. Try using a decision from another workspace and verify rejection before append.
