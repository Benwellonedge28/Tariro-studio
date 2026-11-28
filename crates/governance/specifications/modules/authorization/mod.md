# Authorization service boundary

**ZIP-GOVERNANCE-AUTHORIZATION-MOD-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/authorization/mod.rs`

## Boundary and inputs

Declare separate [assignment grants](assignment.md), [operation claims](operation.md), [one-time approvals](approval.md), [delegation](delegation.md), [expiry](expiry.md) and [revocation](revocation.md). Export typed scoped commands and redacted observations through the owning Governance service. Grant constructors and claimed intent internals remain private.

## Behavior and failure handling

Issuance records permission bounds. Evaluate returns a decision for exact input. Claim serializes current authority and durable intent before any external effect. Only the owning adapter can dispatch under the verified claim. Keep read-only reconciliation and independently authorized cleanup separate. No import or type construction reads credentials, grants authority or executes work.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-MOD-T01.** Compile a downstream fixture that constructs an evaluation input but cannot construct a claimed intent or mutate a grant epoch. Call evaluate with a valid test grant and verify zero effect calls.
