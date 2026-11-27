# Immutable entity identity

**ZIP-KNOWLEDGE-ENTITY-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/entity.rs`

## Required implementation behavior

Bind entity ID, workspace, domain kind, schema/version and pinned source evidence. Conflicting identity requires explicit new revision.

## Acceptance

**ZIP-KNOWLEDGE-ENTITY-T01.** Same display name across domains remains distinct.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
