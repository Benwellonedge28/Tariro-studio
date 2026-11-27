# Repository provider routing

**ZIP-PROVIDERS-REPOSITORIES-MOD-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/repositories/mod.rs`

## Required implementation behavior

Match stable repo ID, pin and operation-specific capability, negotiate scope and version separately from effect authority.

## Acceptance

**ZIP-PROVIDERS-REPOSITORIES-MOD-T01.** Provider registry read cannot push.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
