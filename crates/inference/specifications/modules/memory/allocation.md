# Checked inference memory estimate

**ZIP-INFERENCE-MEMORY-ALLOCATION-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/memory/allocation.rs`

## Required implementation behavior

Reserve model assets, context and runtime overhead before allocation; use checked unit arithmetic and verified cleanup. Unknown required coordinate denies.

## Acceptance

**ZIP-INFERENCE-MEMORY-ALLOCATION-T01.** Overflow and insufficient device memory return distinct typed denial.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
