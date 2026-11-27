# Telemetry failure outcomes

**ZIP-OBSERVABILITY-ERROR-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/error.rs`

## Required implementation behavior

Distinguish unavailable collector, queue full, invalid label, quota, redaction failure and export denial. Audit remains independent.

## Acceptance

**ZIP-OBSERVABILITY-ERROR-T01.** Dropped telemetry does not report committed audit.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
