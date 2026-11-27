# Scheduling deadline calculation

**ZIP-SCHEDULER-DEADLINE-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/deadline.rs`

## Required implementation behavior

Use earliest applicable monotonic deadline; reject expired or overflowing inputs before reservation. Persist restart inputs without pretending process-local instants survive restart.

## Acceptance

**ZIP-SCHEDULER-DEADLINE-T01.** Changing wall-clock time cannot extend an existing live lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
