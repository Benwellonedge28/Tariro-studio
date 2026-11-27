# Scope-bound result cache

**ZIP-INTELLIGENCE-CACHING-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/caching.rs`

## Required implementation behavior

Key reviewed request, provider/model, policy, classification and context digest. Scope and permission revalidate on hit. Never cache unknown completion as success.

## Acceptance

**ZIP-INTELLIGENCE-CACHING-T01.** Identical text across confidential workspaces cannot share cached response.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
