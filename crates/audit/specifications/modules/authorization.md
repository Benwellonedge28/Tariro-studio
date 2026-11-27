# Decision audit binding

**ZIP-AUDIT-AUTHORIZATION-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/authorization.rs`

## Required implementation behavior

Record reviewed policy digest, grant scope digest, decision outcome and revocation epoch. No credential values in archived decision.

## Acceptance

**ZIP-AUDIT-AUTHORIZATION-T01.** Changed policy version yields different attributable decision record.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
