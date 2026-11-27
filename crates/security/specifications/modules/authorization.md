# Default-deny execution gate

**ZIP-SECURITY-AUTHORIZATION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/authorization.rs`

## Required implementation behavior

Intersect current RBAC, ABAC, capability, mandatory policy and grant near effect claim. Check revocation and exact reviewed effect digest. Unknown inputs deny.

## Acceptance

**ZIP-SECURITY-AUTHORIZATION-T01.** Matching role cannot override a denied attribute, stale policy or missing capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
