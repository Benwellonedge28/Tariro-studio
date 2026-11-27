# Ollama service adapter

**ZIP-INFERENCE-BACKENDS-OLLAMA-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/backends/ollama.rs`

## Required implementation behavior

Bind approved local service endpoint and exact model identity. Validate bounded request/stream, no implicit model pulls or remote routing.

## Acceptance

**ZIP-INFERENCE-BACKENDS-OLLAMA-T01.** An unavailable service or alias mismatch cannot initiate a download.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
