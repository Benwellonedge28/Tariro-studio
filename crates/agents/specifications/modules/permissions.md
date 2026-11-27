# Last-moment agent permissions

**ZIP-AGENTS-PERMISSIONS-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/permissions.rs`

## Required implementation behavior

Revalidate scope, grants, current epoch and qualified tool before each effect. Treat discovery as read-only unless separately approved.

## Acceptance

**ZIP-AGENTS-PERMISSIONS-T01.** Revoked grant between planning and dispatch denies execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
