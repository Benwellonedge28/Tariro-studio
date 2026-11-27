# Mistral adapter contract

**ZIP-INFERENCE-BACKENDS-MISTRAL-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/backends/mistral.rs`

## Required implementation behavior

Negotiate exact model/backend config and qualified features; map actual usage and completion. Do not infer support from name alone.

## Acceptance

**ZIP-INFERENCE-BACKENDS-MISTRAL-T01.** Unsupported model context or quantization fails before generation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
