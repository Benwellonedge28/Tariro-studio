# Scope-safe inference telemetry

**ZIP-INFERENCE-METRICS-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/metrics.rs`

## Required implementation behavior

Record observed tokens, duration, admitted/actual capacity and outcome using bounded labels; no prompts or private content. Audit separate.

## Acceptance

**ZIP-INFERENCE-METRICS-T01.** Synthetic prompt canary never appears in metrics export.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
