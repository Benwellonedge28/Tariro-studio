# Scoped clone

**ZIP-REPOSITORY-GIT-CLONE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/clone.rs`

## Required implementation behavior

Validate remote identity, transport and destination before transfer. Preserve partial attempts in private staging and activate only clean verified clone. Do not initialize submodules automatically.

## Acceptance

**ZIP-REPOSITORY-GIT-CLONE-T01.** Failed clone leaves target clean and unapproved submodule URL is unused.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
