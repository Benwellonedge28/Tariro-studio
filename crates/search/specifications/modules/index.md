# Versioned index ownership

**ZIP-SEARCH-INDEX-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/index.rs`

## Required implementation behavior

Bind source generation, index schema, lexical/semantic capabilities and access scope. Publish only after verified staging.

## Acceptance

**ZIP-SEARCH-INDEX-T01.** Failed promotion keeps prior complete generation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
