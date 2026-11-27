# Thermal pressure normalization

**ZIP-RESOURCES-MONITORING-THERMAL-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/monitoring/thermal.rs`

## Required implementation behavior

Map sensor records and capability levels to configured pressure triggers. Unknown sensor never reports cool. Contract does not prescribe hardware-specific degree thresholds.

## Acceptance

**ZIP-RESOURCES-MONITORING-THERMAL-T01.** Sensor missing and policy-matched thermal event produce different outcomes.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
