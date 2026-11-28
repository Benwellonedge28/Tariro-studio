# Audit acceptance fixtures and verdicts

**ZIP-AUDIT-VERIFICATION-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/verification.rs`

## Boundary and inputs

Accept a bounded audit qualification request with candidate digest, authorized scope, expected range, trusted anchors and required evidence references. Verify snapshot integrity under [integrity](integrity.md), then check each required actor, decision, operation and outcome relation independently. Bind the verdict to exact input identities and adapter editions.

## Behavior and failure handling

Return passed for the exact covered requirements, failed for a verified mismatch or violation, and blocked for unavailable anchors, missing observations or unresolved effects. An internally consistent chain can still lack required evidence. Record the first failure and covered range with bounded redacted evidence. Verification changes no durable history or future effect authority.

## Acceptance

**ZIP-AUDIT-VERIFICATION-T01.** Omit an expected outcome record in an otherwise internally consistent slice. Verify acceptance remains blocked. Supply a conflicting anchor and observe failure. Confirm neither run can certify a distinct candidate or workspace.
