# Exact reference provenance

**ZIP-SOURCE-ANALYSIS-REFERENCE-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/reference.rs`

## Required implementation behavior

Bind source range and candidate definition with qualified resolution kind. Preserve unresolved references without fabricating edges.

## Acceptance

**ZIP-SOURCE-ANALYSIS-REFERENCE-T01.** Missing target becomes unresolved rather than a fabricated definition.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
