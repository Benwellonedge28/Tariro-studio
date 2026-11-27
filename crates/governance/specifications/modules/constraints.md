# Scope attenuation and exact rules

**ZIP-GOVERNANCE-CONSTRAINTS-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/constraints.rs`

## Required implementation behavior

Intersect allowed sets, minimum ceilings, earliest expiry and required obligations. Exact assignment constraints must agree. A new subset needs a live parent grant.

## Acceptance

**ZIP-GOVERNANCE-CONSTRAINTS-T01.** Child cannot gain path/destination or raise budget beyond parent.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
