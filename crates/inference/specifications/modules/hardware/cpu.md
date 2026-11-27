# CPU execution budget

**ZIP-INFERENCE-HARDWARE-CPU-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/hardware/cpu.rs`

## Required implementation behavior

Use qualified CPU features and bounded thread/memory requests. Detect capabilities at runtime; deny unsupported required instructions.

## Acceptance

**ZIP-INFERENCE-HARDWARE-CPU-T01.** Low-capacity device reduces admitted batch without profile recompilation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
