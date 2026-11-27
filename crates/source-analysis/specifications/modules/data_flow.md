# Scoped data-flow observations

**ZIP-SOURCE-ANALYSIS-DATA-FLOW-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/data_flow.rs`

## Required implementation behavior

Track declarations, reads, writes and qualified def-use edges over validated flow graph. Annotate uncertainty and bound fixed-point work.

## Acceptance

**ZIP-SOURCE-ANALYSIS-DATA-FLOW-T01.** Iteration exhaustion returns partial analysis, not a proved fact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
