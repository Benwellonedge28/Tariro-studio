# Sandbox capability facade

**ZIP-SANDBOX-LIB-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/lib.rs`

## Required implementation behavior

Expose qualified backend, capability, lifecycle and cleanup handles. Construction without mandatory controls cannot run user work.

## Acceptance

**ZIP-SANDBOX-LIB-T01.** No unrestricted fallback backend is exported.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
