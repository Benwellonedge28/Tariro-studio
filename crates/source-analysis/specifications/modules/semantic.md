# Semantic adapter composition

**ZIP-SOURCE-ANALYSIS-SEMANTIC-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/semantic.rs`

## Required implementation behavior

Merge parse, symbol and type results only at same pinned snapshot. Preserve capability gaps and qualify conflicts instead of guessing.

## Acceptance

**ZIP-SOURCE-ANALYSIS-SEMANTIC-T01.** Mixed revisions are rejected before graph construction.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
