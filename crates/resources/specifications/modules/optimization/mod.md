# Approved optimization boundary

**ZIP-RESOURCES-OPTIMIZATION-MOD-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/optimization/mod.rs`

## Required implementation behavior

Offer proposals for resize, locality routing and eviction. Apply through admission and authorization ports. Resource pressure alone is not permission to egress.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-MOD-T01.** No proposal executes an effect without a refreshed grant and valid lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
