# Versioned policy representation

**ZIP-GOVERNANCE-POLICY-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/policy.rs`

## Required implementation behavior

Represent effect/role scope, deny and allow sets, ceilings, obligations, revision, issuer and compatibility version. Validate before publication and pin digest.

## Acceptance

**ZIP-GOVERNANCE-POLICY-T01.** Malformed candidate cannot replace current generation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
