# Scope-aware retrieval cache

**ZIP-RESEARCH-CACHE-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/cache.rs`

## Required implementation behavior

Key source identity, revision, authorization and response class; TTL and byte cap follow configuration. No broadening scope via hits.

## Acceptance

**ZIP-RESEARCH-CACHE-T01.** Revoked or cross-scope cache entry cannot be returned.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
