# Scoped posting generation

**ZIP-SEARCH-LEXICAL-INVERTED-INDEX-001 · v1.0 · Owner:** Search maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/search/src/lexical/inverted_index.rs`

## Required implementation behavior

Index term and positional records keyed by authorized dataset and snapshot. Rebuild or invalidate affected postings after changes.

## Acceptance

**ZIP-SEARCH-LEXICAL-INVERTED-INDEX-T01.** Deleted record is missing from new generation and retained only per policy.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
