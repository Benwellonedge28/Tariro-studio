# Symbol identity

**ZIP-SOURCE-ANALYSIS-SYMBOL-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/symbol.rs`

## Required implementation behavior

Identify symbol by language, qualified path, defining range, revision and stable kind. Separate declared identity from inferred link.

## Acceptance

**ZIP-SOURCE-ANALYSIS-SYMBOL-T01.** Two same-named functions in separate scopes remain distinct.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
