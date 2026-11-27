# Versioned symbol lookup

**ZIP-SOURCE-ANALYSIS-SYMBOL-TABLE-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/symbol_table.rs`

## Required implementation behavior

Index declarations by normalized name plus scope and revision. Report ties, unknowns and partial adapter coverage. Never expose cross-workspace results.

## Acceptance

**ZIP-SOURCE-ANALYSIS-SYMBOL-TABLE-T01.** Duplicate visible symbol resolves as ambiguous.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
