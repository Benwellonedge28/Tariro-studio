# Priority policy adapter

**ZIP-SCHEDULER-POLICIES-PRIORITY-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/policies/priority.rs`

## Boundary and inputs

Use only the verified priority class in the immutable job and current policy. [Priority](../priority.md) sorts approved larger classes first. Within a class use the persisted workspace fairness cursor, enqueue ordinal and canonical job key. Untrusted descriptions and queue labels never enter the comparator.

## Behavior and failure handling

Read the pinned cursor revision and include it in the proposal, so the Scheduler can reject a stale winner. Advance the cursor only on committed dispatch under the owning Scheduler CAS. A capacity denial keeps the previous cursor and allows a bounded scan of other eligible candidates. This policy promises round-robin service only under the conditions defined by [fairness](../fairness.md).

## Acceptance

**ZIP-SCHEDULER-POLICIES-PRIORITY-T01.** Permute inputs and change only an untrusted task label. The order remains the same. Apply ZIP-SCH-FIX-002 from the [dispatch fixtures](../../../../../contracts/acceptance/scheduler/dispatch-fixtures.json) to check service order before and after restoring the committed cursor.
