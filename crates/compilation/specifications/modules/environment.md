# Hermetic build environment

**ZIP-COMPILATION-ENVIRONMENT-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/environment.rs`

## Required implementation behavior

Use allowlisted variables and pinned inputs only. No inherited credential or network permission. Record digests of relevant values without secrets.

## Acceptance

**ZIP-COMPILATION-ENVIRONMENT-T01.** Parent canary absent from child environment and logs.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
