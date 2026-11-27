# Stable source diagnostics

**ZIP-SOURCE-ANALYSIS-DIAGNOSTICS-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/diagnostics.rs`

## Required implementation behavior

Normalize severity, typed code, source span and adapter/version. Escape unsafe text and bound emitted diagnostics.

## Acceptance

**ZIP-SOURCE-ANALYSIS-DIAGNOSTICS-T01.** Malformed span yields invalid diagnostic rather than invalid indexing.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
