# Measured usage accounting

**ZIP-RESOURCES-MONITORING-UTILIZATION-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/monitoring/utilization.rs`

## Required implementation behavior

Record actual usage against stable pool/attempt identity and sample revision. Distinguish cumulative counters from instantaneous gauges. Reject counter regression without reset/epoch change.

## Acceptance

**ZIP-RESOURCES-MONITORING-UTILIZATION-T01.** Duplicate sample does not charge twice; stale epoch cannot replace live usage.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
