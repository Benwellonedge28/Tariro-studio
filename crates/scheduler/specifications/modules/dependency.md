# Dependency resolution

**ZIP-SCHEDULER-DEPENDENCY-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/dependency.rs`

## Required implementation behavior

Validate graph nodes and reject cycles. Ready requires every mandatory prerequisite's durable verified outcome at the expected revision. Propagate Blocked without scheduling descendants.

## Acceptance

**ZIP-SCHEDULER-DEPENDENCY-T01.** Failure of one prerequisite cannot start the dependent job.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
