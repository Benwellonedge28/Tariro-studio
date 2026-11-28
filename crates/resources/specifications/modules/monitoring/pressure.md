# Pressure coordination

**ZIP-RESOURCES-MONITORING-PRESSURE-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/monitoring/pressure.rs`

## Boundary and inputs

Project a per-pool state using typed fresh observations and a validated policy specifying enter and recovery thresholds, minimum observation counts and the maximum observation age. For increasing pressure signals, enter constrained at or above the configured high threshold and observe recovery at or below the lower threshold. Require strictly ordered thresholds and consecutive qualifying observations. Normalize opposite-direction signals before comparison.

## Behavior and failure handling

An intermediate fresh sample breaks the pending streak and leaves the previously established state unchanged. An unknown or stale input clears the streak and produces unknown evidence. A required unknown hard metric blocks new affected admissions and does not release holds. Publish one revisioned transition and reason per state change. Requests for degrade or drain go through supervising owners. Require fresh observations to reopen constrained intake.

## Acceptance

**ZIP-RESOURCES-MONITORING-PRESSURE-T01.** Oscillate a synthetic signal between thresholds and replay duplicate samples. Verify no extra transition and no false streak advancement. Cross both thresholds with the configured consecutive observations, then inject missing evidence and confirm the remaining hold persists.
