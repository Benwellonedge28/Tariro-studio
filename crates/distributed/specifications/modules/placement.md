# Authorized node selection

**ZIP-DISTRIBUTED-PLACEMENT-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/placement.rs`

## Required implementation behavior

Filter identity, locality, classification, policy, compatibility and available capacity before deterministic scoring.

## Acceptance

**ZIP-DISTRIBUTED-PLACEMENT-T01.** Faster but unapproved node is excluded.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
