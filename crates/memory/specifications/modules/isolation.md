# Tenant cache and index isolation

**ZIP-MEMORY-ISOLATION-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/isolation.rs`

## Required implementation behavior

Key storage, snapshots, caches and access by exact scope; filter before dedupe or ranking. Apply policy to exports too.

## Acceptance

**ZIP-MEMORY-ISOLATION-T01.** Matching digest across tenants does not leak a shared cache hit.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
