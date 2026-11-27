# Pre-ranking filter enforcement

**ZIP-SEARCH-FILTERS-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/filters.rs`

## Required implementation behavior

Apply path/class/scope/retention filters before ranking, cache and snippets. Reject unknown required filter.

## Acceptance

**ZIP-SEARCH-FILTERS-T01.** Hidden private document cannot influence top-k or returned metadata.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
