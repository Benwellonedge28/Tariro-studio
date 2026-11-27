# Gemini adapter boundary

**ZIP-PROVIDERS-INFERENCE-GEMINI-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/gemini.rs`

## Required implementation behavior

Validate qualified modality and request shape, model version and destination policy, and distinguish rejection from complete output.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-GEMINI-T01.** Unsupported modality rejects before data egress.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
