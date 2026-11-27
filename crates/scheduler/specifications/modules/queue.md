# Bounded ready and delayed queue

**ZIP-SCHEDULER-QUEUE-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/queue.rs`

## Required implementation behavior

Enforce workspace item ceilings before insertion; separate delayed from ready by monotonic deadline. Deduplicate by job identity, and rebuild from persisted state.

## Acceptance

**ZIP-SCHEDULER-QUEUE-T01.** Queue-full denial does not drop an existing ready item.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
