# Pinned authorized membership

**ZIP-DISTRIBUTED-MEMBERSHIP-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/membership.rs`

## Required implementation behavior

Apply signed/authenticated membership changes using version and current owner authorization. Fence removed node epochs before allowing further results.

## Acceptance

**ZIP-DISTRIBUTED-MEMBERSHIP-T01.** Revoked member cannot promote a later receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
