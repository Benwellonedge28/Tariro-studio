# Scope-filtered source retrieval

**ZIP-CONTEXT-RETRIEVAL-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/retrieval.rs`

## Required implementation behavior

Resolve workspace and immutable source before search with bounded query. Filter candidates by authorized scope before ranking or using scores.

## Acceptance

**ZIP-CONTEXT-RETRIEVAL-T01.** Cross-workspace data never enters the result set.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
