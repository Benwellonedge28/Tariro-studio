# Changed-object reanalysis

**ZIP-SOURCE-ANALYSIS-INCREMENTAL-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/incremental.rs`

## Required implementation behavior

Diff immutable blob identities, invalidate affected dependencies, reanalyze in stable order and stage atomic generation. Retain prior if interrupted.

## Acceptance

**ZIP-SOURCE-ANALYSIS-INCREMENTAL-T01.** Same changed set produces deterministic new index; stale edges disappear.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
