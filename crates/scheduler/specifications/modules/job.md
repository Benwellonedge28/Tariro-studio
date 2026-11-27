# Immutable scheduled demand

**ZIP-SCHEDULER-JOB-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/job.rs`

## Required implementation behavior

Bind job ID, assignment, plan digest, dependencies, ceiling and deadline. Append attempts under epochs; reject worker results against a different epoch or digest.

## Acceptance

**ZIP-SCHEDULER-JOB-T01.** An expired worker completion cannot replace the active attempt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
