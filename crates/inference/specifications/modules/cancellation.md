# Backend cancellation bridge

**ZIP-INFERENCE-CANCELLATION-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/cancellation.rs`

## Required implementation behavior

Stop new chunks, pass scoped signal, await confirmed session cleanup and preserve partial output or exact receipt. Keep leases while resource remains occupied.

## Acceptance

**ZIP-INFERENCE-CANCELLATION-T01.** Cancelled handle does not imply device memory released.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
