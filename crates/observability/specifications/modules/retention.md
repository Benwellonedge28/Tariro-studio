# Scoped telemetry cleanup

**ZIP-OBSERVABILITY-RETENTION-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/retention.rs`

## Required implementation behavior

Apply configured time/size rules and preserve required durable audit separately. Use bounded reaping with approved storage scope.

## Acceptance

**ZIP-OBSERVABILITY-RETENTION-T01.** Deleting debug logs cannot delete audit evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
