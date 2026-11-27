# Eligible workspace fairness

**ZIP-SCHEDULER-FAIRNESS-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/fairness.rs`

## Required implementation behavior

Within approved priority class choose least recently served eligible workspace, then oldest eligible job, stable ID as tie-breaker. Update cursor only on successful claim. Do not spend fairness turn on denied capacity.

## Acceptance

**ZIP-SCHEDULER-FAIRNESS-T01.** Two continuously eligible equal-priority workspaces alternate accepted claims.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
