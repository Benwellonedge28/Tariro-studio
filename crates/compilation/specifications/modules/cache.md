# Content-addressed build caching

**ZIP-COMPILATION-CACHE-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/cache.rs`

## Required implementation behavior

Key exact tree, toolchain, target, features, dependencies and relevant environment. Promote only verified complete record and check scope on reuse.

## Acceptance

**ZIP-COMPILATION-CACHE-T01.** Failed, partial or stale artifact cannot be returned as hit.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
