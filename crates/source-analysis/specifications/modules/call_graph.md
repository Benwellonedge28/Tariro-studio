# Classified call relationships

**ZIP-SOURCE-ANALYSIS-CALL-GRAPH-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/call_graph.rs`

## Required implementation behavior

Extract qualified direct calls and label dynamic/inferred calls with confidence and source range. Bound traversal and maintain stable edge order.

## Acceptance

**ZIP-SOURCE-ANALYSIS-CALL-GRAPH-T01.** Indirect call never appears as confirmed direct call without evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
