# Repository provider port

**ZIP-REPOSITORY-PROVIDERS-MOD-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/providers/mod.rs`

## Required implementation behavior

Negotiate identity, read/fetch, branch, PR and checks capabilities separately. Normalize effect uncertainty and provider limits. Provider does not grant authority.

## Acceptance

**ZIP-REPOSITORY-PROVIDERS-MOD-T01.** Missing feature remains unavailable instead of selecting a different provider.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
