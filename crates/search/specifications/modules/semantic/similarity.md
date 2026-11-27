# Bounded similarity computation

**ZIP-SEARCH-SEMANTIC-SIMILARITY-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/semantic/similarity.rs`

## Required implementation behavior

Use negotiated metric with compatible vectors, checked finite operations and stable tie-breaker. Report unsupported zero-vector cases per metric.

## Acceptance

**ZIP-SEARCH-SEMANTIC-SIMILARITY-T01.** Undefined relevance never enters results as a plausible score.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
