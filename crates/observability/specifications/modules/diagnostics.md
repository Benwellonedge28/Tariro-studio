# Bounded scoped diagnostics

**ZIP-OBSERVABILITY-DIAGNOSTICS-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/diagnostics.rs`

## Required implementation behavior

Expose redacted actual status and qualified probes with finite output and deadlines. No automatic remote export.

## Acceptance

**ZIP-OBSERVABILITY-DIAGNOSTICS-T01.** Private payload omitted from default diagnostic bundle.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
