# Deterministic coordination round

**ZIP-ORCHESTRATION-COORDINATION-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/coordination.rs`

## Boundary and inputs

A coordination round reads one authorized plan revision, verified readiness set, role catalog and bounded observation snapshot. It returns a deterministic proposal containing ordered eligible task and agent pairs, conflict keys, prerequisites and source revisions. Sort ready tasks by plan rank then stable task identity. Sort equal eligible role candidates by their stable agent identity after approved routing criteria.

## Behavior and failure handling

Exclude out-of-scope agents and known write conflicts before proposing. A missing observation yields a blocked or unavailable task with a bounded typed reason. Record an immutable proposal identity over canonical inputs and selected assignments. Compare the current graph, grant and capacity observations before submission. A proposed pairing has no effect authority and no implied lease. Read-only replay reconstructs the same pair order from the same inputs.

## Acceptance

**ZIP-ORCHESTRATION-COORDINATION-T01.** Permute graph input, role enumeration and agent discovery order. Assert identical scoped proposals. Shift one role or policy revision before application and verify stale input causes fresh evaluation without issuing another command under the old identity.
