# Attenuated delegation

**ZIP-GOVERNANCE-AUTHORIZATION-DELEGATION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/authorization/delegation.rs`

## Required implementation behavior

Intersect child with live parent and enforce policy-derived depth. Persist lineage and expiry; a model/team cannot approve itself or revive revoked lineage.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-DELEGATION-T01.** Delegated publish denied when parent only has inspect permission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
