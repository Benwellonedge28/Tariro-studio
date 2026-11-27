# Device execution negotiation

**ZIP-INFERENCE-HARDWARE-MOD-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/hardware/mod.rs`

## Required implementation behavior

Resolve approved device adapter by enforceable capacity, compatible model and scoped availability. Resource admission remains authoritative.

## Acceptance

**ZIP-INFERENCE-HARDWARE-MOD-T01.** Unsupported accelerator does not automatically imply CPU is usable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
