# Repository command adapter

**ZIP-CLI-COMMANDS-REPOSITORY-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/repository.rs`

## Required implementation behavior

Translate inspect/index/instructions/clone/review into typed gateway commands. Pin requested revision for reads and require approved destination/scope for clone. Never interpolate a command string.

## Acceptance

**ZIP-CLI-COMMANDS-REPOSITORY-T01.** Missing revision or unapproved network path denies the relevant operation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
