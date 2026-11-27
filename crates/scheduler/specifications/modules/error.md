# Decision failure taxonomy

**ZIP-SCHEDULER-ERROR-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/error.rs`

## Required implementation behavior

Distinguish graph cycle, duplicate ID, stale epoch, queue full, missing capacity, expired deadline and uncertain outcome. Include retry hints only after classifying effects.

## Acceptance

**ZIP-SCHEDULER-ERROR-T01.** An uncertain effect cannot be represented as a retryable timeout.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
