# Isolated worktree lifecycle

**ZIP-REPOSITORY-GIT-WORKTREE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/worktree.rs`

## Required implementation behavior

Acquire owned workspace lease, construct dedicated worktree from pinned commit and verify root/head. Cleanup removes only owned staging after preserving work and audit.

## Acceptance

**ZIP-REPOSITORY-GIT-WORKTREE-T01.** A declined force cleanup cannot touch unrelated branches or directories.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
