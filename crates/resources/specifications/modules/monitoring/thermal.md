# Thermal pressure normalization

**ZIP-RESOURCES-MONITORING-THERMAL-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/monitoring/thermal.rs`

## Boundary and inputs

Map a qualified sensor to its host or accelerator accounting identity. Carry the adapter-normalized temperature or pressure category, declared unit, freshness and supported enforcement class. Use only sensors and mappings selected by the resolved thermal policy. Unknown sensors or incompatible metrics yield unknown observations.

## Behavior and failure handling

Where policy uses numeric temperature, reject missing units and failed conversion, then pass a comparable measure to [pressure](pressure.md). Hardware-specific thresholds come from validated policy and may vary by device. Keep emergency platform signals distinct from advisory readings. A validated pressure event requests protective control through its owning supervisor. It never proves teardown or directly changes occupied capacity.

## Acceptance

**ZIP-RESOURCES-MONITORING-THERMAL-T01.** Compare an unavailable sensor, an out-of-range reading and a valid policy-matched thermal event on an enrolled device. Verify cleanly distinct observations, no implicit cool status, and no lease release or mutation initiated by the probe.
