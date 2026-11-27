# Dependency graph semantics

**ZIP-KNOWLEDGE-DOMAINS-DEPENDENCIES-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/domains/dependencies.rs`

## Required implementation behavior

Represent resolved package/version and edge type including target/feature condition. Link to manifest/lock evidence.

## Acceptance

**ZIP-KNOWLEDGE-DOMAINS-DEPENDENCIES-T01.** Missing resolution remains candidate rather than confirmed package.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
