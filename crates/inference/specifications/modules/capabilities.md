# Qualified backend support declaration

**ZIP-INFERENCE-CAPABILITIES-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/capabilities.rs`

## Required implementation behavior

Report supported formats, modalities, context, quantization and cancellation behavior by version and device. Unknown claims deny mandatory capability.

## Acceptance

**ZIP-INFERENCE-CAPABILITIES-T01.** Adapter advertising no cancellation cannot pass task requiring it.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
