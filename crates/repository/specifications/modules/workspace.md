# Worktree and branch ownership

**ZIP-REPOSITORY-WORKSPACE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/workspace.rs`

## Required implementation behavior

Allocate a leased root with pinned base, authorized branch and protected workspace mapping. Check cleanliness and separate repositories during activation.

## Acceptance

**ZIP-REPOSITORY-WORKSPACE-T01.** Parallel assignments cannot overwrite each other's checkout or primary worktree.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
