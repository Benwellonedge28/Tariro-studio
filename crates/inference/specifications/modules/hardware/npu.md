# NPU qualification gate

**ZIP-INFERENCE-HARDWARE-NPU-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/hardware/npu.rs`

## Required implementation behavior

Require supported runtime, model shape and enforceable resource data. Unknown capacity denies required admission.

## Acceptance

**ZIP-INFERENCE-HARDWARE-NPU-T01.** Unavailable driver produces typed unavailability, not optimistic placement.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
