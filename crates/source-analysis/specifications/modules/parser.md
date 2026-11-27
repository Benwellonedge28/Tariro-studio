# Bounded parse port

**ZIP-SOURCE-ANALYSIS-PARSER-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/parser.rs`

## Required implementation behavior

Accept immutable blob, language, qualified grammar version and admitted byte/deadline limits. Return valid, partial or rejected tree with diagnostics.

## Acceptance

**ZIP-SOURCE-ANALYSIS-PARSER-T01.** Invalid UTF-8 never silently alters original spans.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
