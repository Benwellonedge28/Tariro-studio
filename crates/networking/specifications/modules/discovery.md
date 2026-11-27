# Explicit discovery boundary

**ZIP-NETWORKING-DISCOVERY-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/discovery.rs`

## Required implementation behavior

Use approved static or network discovery with a bounded candidate set and scoped records. Discovery confers no access authority.

## Acceptance

**ZIP-NETWORKING-DISCOVERY-T01.** Offline discovery returns only permitted local results.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
