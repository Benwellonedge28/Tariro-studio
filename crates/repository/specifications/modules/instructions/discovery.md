# Applicable instruction paths

**ZIP-REPOSITORY-INSTRUCTIONS-DISCOVERY-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/instructions/discovery.rs`

## Required implementation behavior

For each normalized target file enumerate AGENTS.md at repository root and every ancestor directory of that file. Inspect pinned tree, dedupe paths in deterministic order and distinguish absent from unreadable.

## Acceptance

**ZIP-REPOSITORY-INSTRUCTIONS-DISCOVERY-T01.** Nested instruction discovery reports both root and deepest applicable file.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
