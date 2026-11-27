# Admission pressure handling

**ZIP-SCHEDULER-BACKPRESSURE-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/backpressure.rs`

## Required implementation behavior

Evaluate queue credits and pool pressure before enqueue. Return wait or typed refusal, not silent drop. A waiter respects cancellation and previous admission ownership.

## Acceptance

**ZIP-SCHEDULER-BACKPRESSURE-T01.** Cancel a waiting submitter without consuming a queue slot.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
