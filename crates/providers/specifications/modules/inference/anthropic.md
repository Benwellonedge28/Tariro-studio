# Anthropic adapter boundary

**ZIP-PROVIDERS-INFERENCE-ANTHROPIC-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/anthropic.rs`

## Required implementation behavior

Pin qualified message/stream shape and model identity. Validate admitted response, output limit and terminal status before success.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-ANTHROPIC-T01.** Interrupted stream keeps retained prefix incomplete.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
