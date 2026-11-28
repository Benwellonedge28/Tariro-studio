# Observation ownership

**ZIP-RESOURCES-MONITORING-MOD-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/monitoring/mod.rs`

## Boundary and inputs

Aggregate typed observations from [utilization](utilization.md), [thermal](thermal.md), [battery](battery.md) and [pressure](pressure.md) without changing admission ownership. Every input binds to an enrolled source and a verified attempt or pool, a supported clock domain and a current observation order. Hold a bounded latest-observation and policy view.

## Behavior and failure handling

Reject unknown scopes and stale producer or policy epochs before projecting capacity effects. Publish reason codes and immutable revisions. Only a verified owning path may request fresh admission, cancellation or pressure handling. Monitoring is neither capacity proof on its own nor authority to change quota, credit settlement or executor state. An unavailable observation creates a typed unknown for its scope.

## Acceptance

**ZIP-RESOURCES-MONITORING-MOD-T01.** Send an unknown pool, an old sample and a current scoped input in reverse arrival order. Verify no mutation to ledger holds and only the current observation feeds the decision. Compare the resulting evidence with the resolved policy revision.
