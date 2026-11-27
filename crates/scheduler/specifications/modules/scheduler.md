# Transactional admission loop

**ZIP-SCHEDULER-SCHEDULER-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/scheduler.rs`

## Required implementation behavior

On each wake read ready jobs under the current generation; rank by eligible priority and fairness; reserve capacity then compare-and-swap attempt state. Release an unused reservation when claim loses.

## Acceptance

**ZIP-SCHEDULER-SCHEDULER-T01.** A competing scheduler cannot admit the same attempt twice.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
