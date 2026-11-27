# Stable syntax tree references

**ZIP-SOURCE-ANALYSIS-SYNTAX-TREE-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/syntax_tree.rs`

## Required implementation behavior

Store grammar/version, blob digest, node kind and half-open byte spans. Validate nested intervals and do not retain unbudgeted raw payload.

## Acceptance

**ZIP-SOURCE-ANALYSIS-SYNTAX-TREE-T01.** Out-of-bounds child span is rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
