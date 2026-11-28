# Fenced execution DAG

**ZIP-ORCHESTRATION-EXECUTION-GRAPH-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/execution_graph.rs`

## Boundary and inputs

Bind an immutable graph to its reviewed plan digest and assignment. Each node carries stable task identity, validated dependencies, required role, normalized conflict keys and expected evidence policy. Enforce configured graph budgets before allocation and compile through [dependency_graph](dependency_graph.md) in stable order. Keep mutable progress in revisioned assignment state rather than modifying the compiled graph.

## Behavior and failure handling

Maintain node readiness, pending submission intent and accepted result as distinct observations. Record task and applicable Scheduler claim/attempt identity in assignment-owned durable state. Accept outcome only when plan, graph revision, attempt epoch and trusted evidence match. Reject a stale worker even if its payload matches. Preserve accepted historical outcomes and do not reuse a node identity to change its reviewed intent. Restart reads committed bindings and reconciles pending effects before continuing.

## Acceptance

**ZIP-ORCHESTRATION-EXECUTION-GRAPH-T01.** Compile equal input under two canonical permutations and replay one accepted result. Replan and submit a result from the old graph and epoch. Verify no new progress or outbox evidence is accepted under the new graph.
