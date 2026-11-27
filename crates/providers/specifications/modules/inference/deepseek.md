# DeepSeek adapter boundary

**ZIP-PROVIDERS-INFERENCE-DEEPSEEK-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/deepseek.rs`

## Required implementation behavior

Bind explicit endpoint/model/schema and data/spend scope. Redact sensitive errored request values and retain upstream classification.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-DEEPSEEK-T01.** Denied endpoint sends no prompt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
