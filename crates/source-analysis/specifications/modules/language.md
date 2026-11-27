# Language identity and feature negotiation

**ZIP-SOURCE-ANALYSIS-LANGUAGE-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/language.rs`

## Required implementation behavior

Bind language ID, qualified adapter version and supported analysis features independently. Language availability grants no command execution.

## Acceptance

**ZIP-SOURCE-ANALYSIS-LANGUAGE-T01.** Text fallback advertises no symbol-resolution support.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
