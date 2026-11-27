# Pinned source-code query

**ZIP-SEARCH-CODE-SEARCH-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/code_search.rs`

## Required implementation behavior

Resolve symbols/text against qualified parser and immutable source, validate ranges and mark unresolved semantic matches.

## Acceptance

**ZIP-SEARCH-CODE-SEARCH-T01.** Text-only result never masquerades as resolved symbol.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
