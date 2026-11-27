# Pressure coordination

**ZIP-RESOURCES-MONITORING-PRESSURE-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/monitoring/pressure.rs`

## Required implementation behavior

Use configured thresholds/hysteresis and consecutive fresh observation rules. Transition pools to constrained state, close new intake and request degrade/drain. Emit policy revision and reasons.

## Acceptance

**ZIP-RESOURCES-MONITORING-PRESSURE-T01.** Oscillating samples at boundary do not thrash scheduling or release active leases.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
