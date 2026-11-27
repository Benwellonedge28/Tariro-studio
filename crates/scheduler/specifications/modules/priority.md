# Within-class ordering

**ZIP-SCHEDULER-PRIORITY-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/priority.rs`

## Required implementation behavior

Order permitted priority class, age and then stable ID. Class changes need a reviewed admission input; worker claims cannot self-promote.

## Acceptance

**ZIP-SCHEDULER-PRIORITY-T01.** Input permutation preserves order for tied timestamps.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
