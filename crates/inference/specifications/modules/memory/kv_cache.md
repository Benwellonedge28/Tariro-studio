# Scoped KV-cache accounting

**ZIP-INFERENCE-MEMORY-KV-CACHE-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/memory/kv_cache.rs`

## Required implementation behavior

Bind cached state to session, model/tokenizer, slot and grant. Resize under admitted limit and remove on scope invalidation. Serve no cross-scope entries.

## Acceptance

**ZIP-INFERENCE-MEMORY-KV-CACHE-T01.** A revoked session or changed tokenizer cannot reuse cache.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
