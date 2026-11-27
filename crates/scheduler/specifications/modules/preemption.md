# Controlled draining

**ZIP-SCHEDULER-PREEMPTION-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/preemption.rs`

## Required implementation behavior

Preempt only a policy-eligible attempt at a safe checkpoint or through supervised cancellation. Fence its epoch, preserve outcomes and retain reservations until cleanup.

## Acceptance

**ZIP-SCHEDULER-PREEMPTION-T01.** Preemption during a committed effect preserves its receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
