# Approved history rewrite

**ZIP-REPOSITORY-GIT-REBASE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/rebase.rs`

## Required implementation behavior

Operate on owned worktree only with explicit grant of base/head and controlled conflict policy. Return new candidate for review; no default push follows.

## Acceptance

**ZIP-REPOSITORY-GIT-REBASE-T01.** Rewrite of shared ref is denied, cancellation preserves original ref or recoverable lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
