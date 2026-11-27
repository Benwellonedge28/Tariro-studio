# Conditional branch creation

**ZIP-REPOSITORY-GIT-BRANCH-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/branch.rs`

## Required implementation behavior

Require owned namespace, pinned base and absent target. Verify durable ref from exact remote/local repository after creation. Existing unexpected head conflicts.

## Acceptance

**ZIP-REPOSITORY-GIT-BRANCH-T01.** Same branch name in another repository or prior head cannot be mistaken for success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
