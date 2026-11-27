# Bounded remote reference fetch

**ZIP-REPOSITORY-GIT-FETCH-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/fetch.rs`

## Required implementation behavior

Fetch explicit authorized refs and verify resulting object references under resource limit. No hidden tags/submodule or push effects.

## Acceptance

**ZIP-REPOSITORY-GIT-FETCH-T01.** Unapproved ref fails before network and stale observed target is reported.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
