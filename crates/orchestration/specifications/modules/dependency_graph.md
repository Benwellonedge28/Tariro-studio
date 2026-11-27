# Readiness and invalidation

**ZIP-ORCHESTRATION-DEPENDENCY-GRAPH-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/dependency_graph.rs`

## Required implementation behavior

Compute prerequisites and deterministic readiness, invalidate dependent nodes if required evidence changes. Report missing source IDs.

## Acceptance

**ZIP-ORCHESTRATION-DEPENDENCY-GRAPH-T01.** Dependency failure propagates blocked without starting a dependent node.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
