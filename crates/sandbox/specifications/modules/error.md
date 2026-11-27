# Sandbox failures

**ZIP-SANDBOX-ERROR-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/error.rs`

## Required implementation behavior

Distinguish Unsupported, PolicyDenied, SetupFailed, SpawnFailed, Pressure and CleanupIncomplete. Keep artifact/lease IDs but redact host paths.

## Acceptance

**ZIP-SANDBOX-ERROR-T01.** Child exited but descendants live yields incomplete cleanup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
