# Search service boundary

**ZIP-SEARCH-LIB-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/lib.rs`

## Required implementation behavior

Expose query, index, authorization-aware results and cursors without reading content until requested.

## Acceptance

**ZIP-SEARCH-LIB-T01.** Facade fixture performs no index acquisition outside explicit call.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
