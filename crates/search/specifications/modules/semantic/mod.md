# Semantic pipeline boundary

**ZIP-SEARCH-SEMANTIC-MOD-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/semantic/mod.rs`

## Required implementation behavior

Resolve versioned embedding, vector and similarity components. Respect allowed egress and budget before generating vectors.

## Acceptance

**ZIP-SEARCH-SEMANTIC-MOD-T01.** Missing local model cannot trigger unapproved external embedding.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
