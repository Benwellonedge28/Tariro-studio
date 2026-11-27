# Research evidence failure classes

**ZIP-RESEARCH-ERROR-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/error.rs`

## Required implementation behavior

Distinguish denied destination, unavailable source, oversized payload, stale citation, contradictory evidence and incomplete scope.

## Acceptance

**ZIP-RESEARCH-ERROR-T01.** Failed retrieval never becomes a directly observed citation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
