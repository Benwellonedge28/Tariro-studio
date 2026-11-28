# Bounded execution telemetry

**ZIP-RUNTIME-METRICS-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/metrics.rs`

## Boundary and inputs

Record bounded runtime counters and timings through a composition-supplied instrumentation sink. Metrics accept only fixed lifecycle, operation and runtime error categories. Measure elapsed time in the active monotonic domain and let the approved sink own histogram configuration. Include count of current held or recovering attempts only from the corresponding trusted snapshot. Bound queue bytes and items by the admitted sink budget.

## Behavior and failure handling

Count accepted lifecycle and attempt transitions from their committed observations. A replay receipt must never be counted as a new transition. Increment a best-effort event counter at most once per committed provenance within the live instrumentation view, without a growing task-ID cache. Surface sink loss through a bounded drop signal when available. Metrics may reset on new process ownership and do not supply durable acceptance. Keep paths, payloads, provider details, task IDs and arbitrary error messages out of labels. Export no external sample without separately authorized observability wiring.

## Acceptance

**ZIP-RUNTIME-METRICS-T01.** Feed varying task identifiers and strings into equivalent events and observe the same fixed series. Replay one committed receipt, fail the sink and restart. Verify no duplicate count within the view, no blocked journal progression and no sensitive sample or label.
