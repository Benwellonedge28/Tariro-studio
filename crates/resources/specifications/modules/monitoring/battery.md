# Power constraint profile

**ZIP-RESOURCES-MONITORING-BATTERY-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/monitoring/battery.rs`

## Required implementation behavior

Track plugged, battery, unknown and capability-supported estimates. Apply owner-approved policies to future admissions and emit pressure signal for running work.

## Acceptance

**ZIP-RESOURCES-MONITORING-BATTERY-T01.** Power supply loss applies profile reduction without widening permissions or silently canceling durable work.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
