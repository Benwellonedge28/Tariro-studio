# Windows process and path containment

**ZIP-SANDBOX-BACKENDS-WINDOWS-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/backends/windows.rs`

## Required implementation behavior

Qualify process-tree control and filesystem identity with Windows-specific adapters. Deny untrusted writes where reparse or scope proof is missing.

## Acceptance

**ZIP-SANDBOX-BACKENDS-WINDOWS-T01.** Process-tree cleanup and reparse-point denial are required before advertising feature.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
