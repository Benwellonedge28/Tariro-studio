# Inference adapter negotiation

**ZIP-PROVIDERS-INFERENCE-MOD-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/mod.rs`

## Required implementation behavior

Resolve exact adapter, model/tokenizer capability, data scope and budget before invocation. Preserve failure and partial output status.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-MOD-T01.** Unsupported provider version cannot dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
