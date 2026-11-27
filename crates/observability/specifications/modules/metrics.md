# Finite metrics series

**ZIP-OBSERVABILITY-METRICS-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/metrics.rs`

## Required implementation behavior

Use approved dimensions, configured cardinality and bounded queues. Separate actual measurement from estimate and drop excess with counters.

## Acceptance

**ZIP-OBSERVABILITY-METRICS-T01.** High cardinality tags do not exceed configured series budget.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
