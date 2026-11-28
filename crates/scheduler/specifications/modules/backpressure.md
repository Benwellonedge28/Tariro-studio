# Admission pressure handling

**ZIP-SCHEDULER-BACKPRESSURE-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/backpressure.rs`

## Boundary and inputs

Accept an authorized enqueue intent, observed queue revision and a bounded optional wait supplied by the caller. Return the committed existing receipt for an exact replay. The [queue](queue.md) owns item accounting and commits an admission against the resolved workspace cap. A read-only observation of pressure or available credits never reserves an item.

## Behavior and failure handling

Distinguish a known full workspace from a wait for a changed queue state. Observe the queue generation, register a bounded waiter and recheck the generation before sleeping to avoid missed wakes. Waiters carry no queue slot or lease. On wake revalidate authority, request identity and deadline before the enqueue CAS. Cancelled waits unregister only themselves. If an insert already committed before a response was lost, recover its receipt through the original key. A pressure-deferred job already in the queue remains one item.

## Acceptance

**ZIP-SCHEDULER-BACKPRESSURE-T01.** Race two writers for the last slot in ZIP-SCH-FIX-007 of the [dispatch fixtures](../../../../contracts/acceptance/scheduler/dispatch-fixtures.json). Cancel a waiting submitter and verify no queue slot was charged. Replay the winner and verify the same receipt without another insertion.
