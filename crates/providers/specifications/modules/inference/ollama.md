# Ollama adapter boundary

**ZIP-PROVIDERS-INFERENCE-OLLAMA-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/inference/ollama.rs`

## Required implementation behavior

Use explicitly approved local service and verified model/configuration. No automatic catalog download, implicit pull or hosted fallback.

## Acceptance

**ZIP-PROVIDERS-INFERENCE-OLLAMA-T01.** Missing local model reports unavailable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
