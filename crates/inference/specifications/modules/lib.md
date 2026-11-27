# Inference backend boundary

**ZIP-INFERENCE-LIB-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/lib.rs`

## Required implementation behavior

Expose engine, sessions, request/result and telemetry ports; adapter initialization is injected and authority-scoped.

## Acceptance

**ZIP-INFERENCE-LIB-T01.** Construct metadata reader without loading model or contacting service.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
