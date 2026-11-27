# Repository role

**ZIP-AGENTS-ROLES-REPOSITORY-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/repository.rs`

## Required implementation behavior

Inspect pinned snapshots, plan reviewed refs/diff and surface reconcile outcomes. No default force push, merge or release authority.

## Acceptance

**ZIP-AGENTS-ROLES-REPOSITORY-T01.** Changed remote ref triggers conflict, not blind overwrite.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
