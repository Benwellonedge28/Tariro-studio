# Exact change evidence

**ZIP-VERIFICATION-REPOSITORY-DIFF-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/repository/diff.rs`

## Required implementation behavior

Compare pinned base/head and inspect normalized before/after paths, mode and digest. Fail partial diff and report unsupported operations explicitly.

## Acceptance

**ZIP-VERIFICATION-REPOSITORY-DIFF-T01.** A truncated diff cannot certify changed paths.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
