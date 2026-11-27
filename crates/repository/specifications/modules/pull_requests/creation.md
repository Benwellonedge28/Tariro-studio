# Guarded pull request creation

**ZIP-REPOSITORY-PULL-REQUESTS-CREATION-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/pull_requests/creation.rs`

## Required implementation behavior

Seal provider repo ID, base/head refs and digests, stable effect marker and title/body policy. Recheck expected heads and approval, record intent, create once and verify actual receipt.

## Acceptance

**ZIP-REPOSITORY-PULL-REQUESTS-CREATION-T01.** Lost create response locates exact PR by immutable identifiers instead of reposting.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
