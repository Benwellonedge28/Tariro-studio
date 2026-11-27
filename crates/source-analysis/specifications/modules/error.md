# Analysis failure classes

**ZIP-SOURCE-ANALYSIS-ERROR-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/error.rs`

## Required implementation behavior

Distinguish unsupported language, malformed input, budget, stale revision, partial analysis and adapter failure. Keep source payload out of errors.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ERROR-T01.** Timeout returns incomplete coverage rather than an empty successful graph.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
