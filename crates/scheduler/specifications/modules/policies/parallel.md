# Admitted parallel placement

**ZIP-SCHEDULER-POLICIES-PARALLEL-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/policies/parallel.rs`

## Required implementation behavior

Request capacity for each independent eligible job. Track conflict keys and deny overlap within a write scope. Stop when leases or queue budgets are exhausted.

## Acceptance

**ZIP-SCHEDULER-POLICIES-PARALLEL-T01.** Independent jobs proceed; jobs with same write conflict key serialize.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
