# Workspace membership boundary

**ZIP-IDENTITY-WORKSPACE-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/workspace.rs`

## Required implementation behavior

Resolve principal/workspace membership at pinned revision and verify current status before effects. Do not project unrelated memberships.

## Acceptance

**ZIP-IDENTITY-WORKSPACE-T01.** Removed membership invalidates cached scoped permission.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
