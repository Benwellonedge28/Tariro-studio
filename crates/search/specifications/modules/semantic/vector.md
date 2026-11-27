# Vector representation gate

**ZIP-SEARCH-SEMANTIC-VECTOR-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/semantic/vector.rs`

## Required implementation behavior

Validate qualified dimension, finite components and metric preconditions. No coercion between incompatible representations.

## Acceptance

**ZIP-SEARCH-SEMANTIC-VECTOR-T01.** Mismatched dimension rejects before matrix computation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
