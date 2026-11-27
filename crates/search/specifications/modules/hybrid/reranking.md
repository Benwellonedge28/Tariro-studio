# Admitted rerank stage

**ZIP-SEARCH-HYBRID-RERANKING-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/hybrid/reranking.rs`

## Required implementation behavior

Rerank bounded authorized candidates with pinned scorer and results. No silent provider escalation on budget/failure.

## Acceptance

**ZIP-SEARCH-HYBRID-RERANKING-T01.** Remote-only scorer unavailable under offline scope.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
