# Attenuated principal authority

**ZIP-IDENTITY-DELEGATION-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/delegation.rs`

## Required implementation behavior

Require live parent lineage, verified child identity and policy-based intersection of effects, targets and expiry; block cycles.

## Acceptance

**ZIP-IDENTITY-DELEGATION-T01.** Child cannot use a broader destination or survive revoked parent.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
