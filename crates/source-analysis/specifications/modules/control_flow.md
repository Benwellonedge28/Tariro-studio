# Qualified control-flow model

**ZIP-SOURCE-ANALYSIS-CONTROL-FLOW-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/control_flow.rs`

## Required implementation behavior

Map supported syntax to explicit entry, branch, exit and unknown edges. Validate target IDs and bound node expansion.

## Acceptance

**ZIP-SOURCE-ANALYSIS-CONTROL-FLOW-T01.** Unsupported statement never becomes an always-false branch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
