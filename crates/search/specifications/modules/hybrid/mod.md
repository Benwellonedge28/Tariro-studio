# Hybrid search composition

**ZIP-SEARCH-HYBRID-MOD-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/hybrid/mod.rs`

## Required implementation behavior

Combine qualified lexical and semantic results only for matching scope/source generation. Missing optional capability remains explicit.

## Acceptance

**ZIP-SEARCH-HYBRID-MOD-T01.** Mismatched generations cannot be fused as current results.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
