# Approved remote device placement

**ZIP-INFERENCE-HARDWARE-DISTRIBUTED-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/hardware/distributed.rs`

## Required implementation behavior

Pin authenticated worker, scope and epoch; negotiate capacity and authorize exact data transfer before requesting execution.

## Acceptance

**ZIP-INFERENCE-HARDWARE-DISTRIBUTED-T01.** Stale remote worker cannot produce current verified result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
