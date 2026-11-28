# Power constraint profile

**ZIP-RESOURCES-MONITORING-BATTERY-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/monitoring/battery.rs`

## Boundary and inputs

Read qualified local power observations from the injected adapter. Represent external power, battery and unknown as distinct source states. Attach sample clock domain, freshness and any adapter-qualified remaining charge estimate with explicit units. An unknown estimate does not imply depleted or fully charged.

## Behavior and failure handling

Apply the resolved policy for the observed source as an input to future admission decisions. A loss of external power may request bounded degradation or drain under current supervision. Emit a revisioned pressure input for running work. Battery monitoring has no authority to cancel assignments, settle usage or release holds. A missing sensor follows the configured unknown policy rather than inheriting the previous plugged reading.

## Acceptance

**ZIP-RESOURCES-MONITORING-BATTERY-T01.** Switch a synthetic host from external power to battery to unknown. Verify a configured future-admission reduction, preserved durable attempts and no increase in policy rights. Invalid units and stale power samples cannot produce a new trusted observation.
