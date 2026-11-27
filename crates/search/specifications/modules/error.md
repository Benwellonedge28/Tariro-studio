# Search failure taxonomy

**ZIP-SEARCH-ERROR-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/error.rs`

## Required implementation behavior

Classify invalid query, denied scope, stale cursor, unavailable index, incompatible embedding, quota and partial scan.

## Acceptance

**ZIP-SEARCH-ERROR-T01.** Error conceals inaccessible index identities.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
