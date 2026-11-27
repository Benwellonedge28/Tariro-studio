# Distributed execution failures

**ZIP-DISTRIBUTED-ERROR-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/error.rs`

## Required implementation behavior

Distinguish rejected membership, stale epoch, expired lease, unavailable capability, partition, bad artifact and uncertain effect.

## Acceptance

**ZIP-DISTRIBUTED-ERROR-T01.** A partition never implies remote task definitely failed.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
