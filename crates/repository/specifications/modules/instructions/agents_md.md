# Bounded instruction read

**ZIP-REPOSITORY-INSTRUCTIONS-AGENTS-MD-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/instructions/agents_md.rs`

## Required implementation behavior

Read scoped regular UTF-8 blob under admitted budget and preserve source hash/path. Treat text as untrusted lower-authority constraints. Unreadable required text blocks affected work.

## Acceptance

**ZIP-REPOSITORY-INSTRUCTIONS-AGENTS-MD-T01.** Invalid UTF-8 and symlink candidate deny instruction satisfaction.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
