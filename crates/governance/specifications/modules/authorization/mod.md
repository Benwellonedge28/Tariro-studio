# Authorization service boundary

**ZIP-GOVERNANCE-AUTHORIZATION-MOD-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/authorization/mod.rs`

## Required implementation behavior

Export separate assignment, operation, approval, delegation, expiry and revoke ports. Keep effect execution outside authority issuance.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-MOD-T01.** A consumer cannot execute effects from a grant constructor alone.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
