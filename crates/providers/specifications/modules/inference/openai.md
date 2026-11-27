# OpenAI adapter boundary

**ZIP-PROVIDERS-INFERENCE-OPENAI-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/openai.rs`

## Required implementation behavior

Qualify documented operation, model and schema against pinned adapter version. Require exact endpoint, credential and disclosure authorization; preserve usage/finish evidence.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-OPENAI-T01.** Missing usage remains unresolved, not zero or complete.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
