# File operation authorization

**ZIP-FILESYSTEM-PERMISSIONS-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/permissions.rs`

## Required implementation behavior

Obtain an effect-specific permission using current actor, scope, revision and requested operation; target existence is disclosed only to authorized readers.

## Acceptance

**ZIP-FILESYSTEM-PERMISSIONS-T01.** An unauthorized caller cannot differentiate an existing secret path from an absent one.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
