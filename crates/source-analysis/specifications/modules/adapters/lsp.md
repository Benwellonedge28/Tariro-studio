# Scoped LSP client bridge

**ZIP-SOURCE-ANALYSIS-ADAPTERS-LSP-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/lsp.rs`

## Required implementation behavior

Negotiate capabilities and position encoding, validate server identity and exact document versions. Convert ranges to source bytes with guards.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-LSP-T01.** Stale server diagnostic or conflicting range encoding does not enter current index.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
