# Repository verification service

**ZIP-VERIFICATION-REPOSITORY-MOD-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/repository/mod.rs`

## Required implementation behavior

Expose diff, scope, batch and integration checks for exact pinned repository. No operation writes a branch or PR.

## Acceptance

**ZIP-VERIFICATION-REPOSITORY-MOD-T01.** Checking a candidate produces evidence and no mutation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
