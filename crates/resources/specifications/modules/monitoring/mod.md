# Observation ownership

**ZIP-RESOURCES-MONITORING-MOD-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/monitoring/mod.rs`

## Required implementation behavior

Expose typed usage, thermal, battery and pressure input ports. Monitoring can request re-admission but cannot expand quota or release a lease.

## Acceptance

**ZIP-RESOURCES-MONITORING-MOD-T01.** Observation with unknown resource scope cannot mutate pool totals.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
