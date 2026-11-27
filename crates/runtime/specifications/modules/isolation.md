# Execution capability check

**ZIP-RUNTIME-ISOLATION-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/isolation.rs`

## Required implementation behavior

Verify required containment from selected platform adapter for filesystem, process, resource and network policy. Never use unconfined fallback when lease requires a sandbox.

## Acceptance

**ZIP-RUNTIME-ISOLATION-T01.** Unsupported platform cannot spawn untrusted task despite sufficient capacity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
