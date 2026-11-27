# Priority policy adapter

**ZIP-SCHEDULER-POLICIES-PRIORITY-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/policies/priority.rs`

## Required implementation behavior

Apply the approved class and stable ordering, preserving fairness within class. Never interpret task-provided labels as authorization.

## Acceptance

**ZIP-SCHEDULER-POLICIES-PRIORITY-T01.** Changing an untrusted task label does not change priority.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
