# Admitted inference engine

**ZIP-INFERENCE-ENGINE-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/engine.rs`

## Required implementation behavior

Validate model/tokenizer identity, effective context and output limits, device capability and live lease. Dispatch bounded session; preserve cleanup obligation.

## Acceptance

**ZIP-INFERENCE-ENGINE-T01.** Oversize request is denied before backend allocation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
