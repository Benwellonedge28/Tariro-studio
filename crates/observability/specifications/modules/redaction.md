# Telemetry field protection

**ZIP-OBSERVABILITY-REDACTION-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/redaction.rs`

## Required implementation behavior

Allowlist stable data fields, omit secret-bearing/raw unknown values before queue/export, preserve safe correlation.

## Acceptance

**ZIP-OBSERVABILITY-REDACTION-T01.** Synthetic canary absent across logs, traces and exported metrics.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
