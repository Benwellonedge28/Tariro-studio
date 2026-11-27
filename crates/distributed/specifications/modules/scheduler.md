# Revision-checked remote claim

**ZIP-DISTRIBUTED-SCHEDULER-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/scheduler.rs`

## Required implementation behavior

Choose ready reviewed task, obtain admitted node lease and claim under current epoch. Compensate unused reservations only after proof.

## Acceptance

**ZIP-DISTRIBUTED-SCHEDULER-T01.** Two coordinators racing cannot issue independently valid epochs for the same task.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
