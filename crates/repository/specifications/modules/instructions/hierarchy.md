# Ancestor applicability

**ZIP-REPOSITORY-INSTRUCTIONS-HIERARCHY-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/instructions/hierarchy.rs`

## Required implementation behavior

Associate a candidate path with applicable ancestor scopes using normalized components. File path, not string prefix, defines containment. More specific content is reviewed alongside all higher scopes.

## Acceptance

**ZIP-REPOSITORY-INSTRUCTIONS-HIERARCHY-T01.** docs-private does not inherit docs instruction by textual similarity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
