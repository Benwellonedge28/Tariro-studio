# Resource-scored policy adapter

**ZIP-SCHEDULER-POLICIES-RESOURCE-AWARE-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/policies/resource_aware.rs`

## Required implementation behavior

Rank qualified placements by finite headroom after demand and configured stable tie-breaker; reject unknown required capacity.

## Acceptance

**ZIP-SCHEDULER-POLICIES-RESOURCE-AWARE-T01.** Missing GPU telemetry cannot outrank an enforceable local pool.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
