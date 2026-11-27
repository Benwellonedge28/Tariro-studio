# Tree-sitter grammar bridge

**ZIP-SOURCE-ANALYSIS-ADAPTERS-TREE-SITTER-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/tree_sitter.rs`

## Required implementation behavior

Pin grammar revision, feed bounded source and normalize actual ranges and parse error nodes without executing candidate code.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-TREE-SITTER-T01.** Malformed grammar/source never yields a fully valid claim.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
