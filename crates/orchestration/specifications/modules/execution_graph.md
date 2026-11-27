# Fenced execution DAG

**ZIP-ORCHESTRATION-EXECUTION-GRAPH-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/execution_graph.rs`

## Required implementation behavior

Pin task IDs, transitions, outputs and admission, enforce graph acyclicity and stable order, persist child outcome only if epoch and plan match.

## Acceptance

**ZIP-ORCHESTRATION-EXECUTION-GRAPH-T01.** Worker from old plan cannot complete current graph node.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
