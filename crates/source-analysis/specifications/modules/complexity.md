# Comparable complexity measures

**ZIP-SOURCE-ANALYSIS-COMPLEXITY-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/complexity.rs`

## Required implementation behavior

Record metric kind, adapter/algorithm and revision. Bound scan and return unsupported for syntax outside profile.

## Acceptance

**ZIP-SOURCE-ANALYSIS-COMPLEXITY-T01.** Same fixture produces same measure and unsupported grammar yields no score.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
