# Qualified local alert rules

**ZIP-OBSERVABILITY-ALERTS-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/alerts.rs`

## Required implementation behavior

Evaluate versioned thresholds and time windows from trusted observations, then dedupe and route through approved notification scope.

## Acceptance

**ZIP-OBSERVABILITY-ALERTS-T01.** Alert cannot transmit externally under local-only profile.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
