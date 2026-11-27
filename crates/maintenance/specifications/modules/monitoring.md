# Qualified maintenance observations

**ZIP-MAINTENANCE-MONITORING-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/monitoring.rs`

## Required implementation behavior

Collect scoped resource, revision and lifecycle signals without mutation; distinguish stale and missing signals. Apply approved cadence and finite limits.

## Acceptance

**ZIP-MAINTENANCE-MONITORING-T01.** Stale disk report cannot authorize deletion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
