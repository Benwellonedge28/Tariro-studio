# Versioned embedding ingestion

**ZIP-SEARCH-SEMANTIC-EMBEDDINGS-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/semantic/embeddings.rs`

## Required implementation behavior

Bind source digest, model/tokenizer version, vector dimensions and authority. Validate shape and finite values before indexing.

## Acceptance

**ZIP-SEARCH-SEMANTIC-EMBEDDINGS-T01.** NaN, dimension mismatch and unauthorized source denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
