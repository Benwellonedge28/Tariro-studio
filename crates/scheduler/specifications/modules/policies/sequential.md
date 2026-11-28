# Serial placement profile

**ZIP-SCHEDULER-POLICIES-SEQUENTIAL-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/policies/sequential.rs`

## Boundary and inputs

Scope serial selection to the exact assignment or tighter policy boundary from the pinned plan. Use current [queue](../queue.md) readiness and fairness order. Before proposing one eligible job, verify that the same scope has no claimed, attached, draining or unresolved attempt occupying its serial slot.

## Behavior and failure handling

Use a trusted claim revision and the supervisor's current settlement evidence. A released worker handle or timed-out wait does not free the serial slot. Atomically enforce exclusive use at the owning claim and launch gates. Only verified teardown plus required reconciliation permits the next proposal. Cancellation affects the selected attempt through its normal control path.

## Acceptance

**ZIP-SCHEDULER-POLICIES-SEQUENTIAL-T01.** Keep one attempt in recovery with an unreaped child. Verify serial policy proposes no successor even when spare workers are available. Reconcile release and verify only the highest-ranked eligible next job is proposed.
