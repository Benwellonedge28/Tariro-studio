# Model command adapter

**ZIP-CLI-COMMANDS-MODEL-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/model.rs`

## Required implementation behavior

Translate manifest lookup, import/download, load/unload and benchmark into typed model operations. Network downloads and hardware leases are separately approved.

## Acceptance

**ZIP-CLI-COMMANDS-MODEL-T01.** Offline import succeeds from approved local file while unapproved download is denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
