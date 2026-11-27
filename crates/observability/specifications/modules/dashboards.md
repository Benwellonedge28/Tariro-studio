# Bounded read-model projections

**ZIP-OBSERVABILITY-DASHBOARDS-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/dashboards.rs`

## Required implementation behavior

Query authorized redacted metrics, preserve stale/missing status and require pagination/cardinality checks. Dashboards are read-only by default.

## Acceptance

**ZIP-OBSERVABILITY-DASHBOARDS-T01.** Missing observation appears unknown, not as zero.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
