# Scoped vector index

**ZIP-SEARCH-SEMANTIC-INDEX-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/semantic/index.rs`

## Required implementation behavior

Separate model/dimension/scope generations, check access before candidate collection and report approximation parameters/truncation.

## Acceptance

**ZIP-SEARCH-SEMANTIC-INDEX-T01.** Incompatible embedding schemas never share a candidate set.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
