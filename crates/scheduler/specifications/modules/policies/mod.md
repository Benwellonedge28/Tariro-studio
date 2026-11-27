# Pure policy dispatch

**ZIP-SCHEDULER-POLICIES-MOD-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/policies/mod.rs`

## Required implementation behavior

Select a supported policy from validated configuration, evaluate snapshots and return ranked proposals. Effect authority remains at admission.

## Acceptance

**ZIP-SCHEDULER-POLICIES-MOD-T01.** Missing policy does not fall back to an unrestricted scheduler.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
