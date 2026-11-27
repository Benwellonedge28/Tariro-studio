# Explicit conflict state

**ZIP-REPOSITORY-GIT-CONFLICT-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/conflict.rs`

## Required implementation behavior

Return normalized path and base/ours/theirs object refs under access limits. Preserve conflict state and require reviewed resolution. Never silently choose a side.

## Acceptance

**ZIP-REPOSITORY-GIT-CONFLICT-T01.** Cancel during conflict keeps original confirmed ref and reports unresolved files.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
