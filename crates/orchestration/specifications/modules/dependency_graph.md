# Readiness and invalidation

**ZIP-ORCHESTRATION-DEPENDENCY-GRAPH-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/dependency_graph.rs`

## Boundary and inputs

Construct a bounded acyclic dependency view over stable task identifiers and required evidence bindings. Check duplicate nodes or edges, unknown endpoints, self edges and plan scope before exposing a graph. Use topological traversal with canonical ready ordering. Read receipt identities from one pinned provenance snapshot and report missing identifiers only to authorized diagnostics.

## Behavior and failure handling

A node is ready when each required predecessor has a verified success at the expected binding. Unresolved results stay pending. A definitive prerequisite failure blocks dependent nodes. When a referenced evidence digest changes or loses validity, recompute only the affected descendants in canonical order under the graph revision. Do not erase already committed evidence or silently rerun an active node. Invalidated active work follows supervisor fencing and settlement.

## Acceptance

**ZIP-ORCHESTRATION-DEPENDENCY-GRAPH-T01.** Test a cycle, foreign node and missing proof. Then change a required proof after one branch becomes ready. Its descendants are blocked or fenced under scope while an independent branch remains eligible. Verify no scheduler submissions come from an unvalidated graph.
