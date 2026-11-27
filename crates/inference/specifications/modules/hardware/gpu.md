# GPU device-specific placement

**ZIP-INFERENCE-HARDWARE-GPU-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/hardware/gpu.rs`

## Required implementation behavior

Compare model demand with approved accelerator's available memory and device capabilities. Avoid summing disjoint pools without qualified sharding.

## Acceptance

**ZIP-INFERENCE-HARDWARE-GPU-T01.** Combined VRAM cannot admit single-device workload larger than each pool.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
