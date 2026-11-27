# Streaming model integrity

**ZIP-MODELS-INTEGRITY-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/integrity.rs`

## Required implementation behavior

Verify expected bytes and shard digests under admitted memory/storage bounds. No model handle before all required assets verified.

## Acceptance

**ZIP-MODELS-INTEGRITY-T01.** Single-byte divergence and incomplete shard each block readiness.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
