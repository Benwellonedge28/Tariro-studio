# Reviewed commit

**ZIP-REPOSITORY-GIT-COMMIT-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/commit.rs`

## Required implementation behavior

Verify staged diff digest and expected parent, preserve author provenance, create commit and confirm tree/parent. Repository content cannot enable hooks.

## Acceptance

**ZIP-REPOSITORY-GIT-COMMIT-T01.** Modify staged file after review and decline commit without consuming authorization.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
