# Active node registry

**ZIP-DISTRIBUTED-REGISTRY-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/registry.rs`

## Required implementation behavior

Index stable IDs and latest authenticated generations; reject stale or conflicting adverts. Preserve unavailable status for unqualified capabilities.

## Acceptance

**ZIP-DISTRIBUTED-REGISTRY-T01.** Older advertisement cannot revive removed capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
