# Readiness projection

**ZIP-RUNTIME-HEALTH-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/health.rs`

## Required implementation behavior

Evaluate lifecycle, storage, availability of mandatory adapters and unresolved recovery prerequisites. Expose bounded failure codes without personal data. Health is read-only.

## Acceptance

**ZIP-RUNTIME-HEALTH-T01.** Failed storage or reconciliation makes readiness false while liveness remains observable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
