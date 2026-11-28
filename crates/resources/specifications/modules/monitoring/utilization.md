# Measured usage accounting

**ZIP-RESOURCES-MONITORING-UTILIZATION-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/monitoring/utilization.rs`

## Boundary and inputs

Accept structured trusted samples keyed by source, physical pool, attempt when known, sample revision and collector epoch. Keep cumulative counters and instantaneous gauges distinct. Reject unsupported units and scope mismatches. A counter delta requires a current baseline in the same epoch and monotonic sample and counter progression. A validated new epoch establishes a new baseline with no retroactive increment.

## Behavior and failure handling

Ignore an identical replay and deny a conflicting payload for the same revision. Drop a stale producer epoch. Gauges inform monitoring without becoming charges. For a metered resource, an adapter must independently qualify evidence and submit the ordered UsageDelta through [admission](../admission.md). There is no second charge path in Monitoring. Preserve bounded summaries and exclude tenant payloads.

## Acceptance

**ZIP-RESOURCES-MONITORING-UTILIZATION-T01.** Send an identical and conflicting sample at one revision, a regression in the same epoch, and a qualified new baseline. Assert at most one accepted observation per identity, zero charging from the sampler, and no change to live usage from stale input.
