# Atomic index generation

**ZIP-SOURCE-ANALYSIS-INDEXING-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/indexing.rs`

## Required implementation behavior

Stage analyzed blobs and dependency updates under a new immutable generation. Activate only after validating scope, completeness and source revision.

## Acceptance

**ZIP-SOURCE-ANALYSIS-INDEXING-T01.** Crash before publication leaves prior index readable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
