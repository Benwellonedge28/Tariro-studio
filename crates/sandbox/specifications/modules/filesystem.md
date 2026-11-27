# Sandbox filesystem policy adapter

**ZIP-SANDBOX-FILESYSTEM-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/filesystem.rs`

## Required implementation behavior

Map admitted root permissions to backend handles without inheriting arbitrary mounts. Resolve links and identities through approved capabilities.

## Acceptance

**ZIP-SANDBOX-FILESYSTEM-T01.** Outside-scope path cannot be opened after staging a permitted workspace.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
