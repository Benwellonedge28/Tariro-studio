# Server command adapter

**ZIP-CLI-COMMANDS-SERVER-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/server.rs`

## Required implementation behavior

Start through runtime or approved service supervisor, verify loopback and profile, and stop by owned service ID. Requesting remote binding is a separate scope.

## Acceptance

**ZIP-CLI-COMMANDS-SERVER-T01.** Default startup creates no remote listener; stale service identity cannot terminate unrelated process.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
