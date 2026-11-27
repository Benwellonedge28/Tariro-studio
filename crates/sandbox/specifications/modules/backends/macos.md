# macOS isolation capability

**ZIP-SANDBOX-BACKENDS-MACOS-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/backends/macos.rs`

## Required implementation behavior

Expose only capabilities proven by platform-specific adapters and test fixtures. Required filesystem or network control unavailable prevents spawn.

## Acceptance

**ZIP-SANDBOX-BACKENDS-MACOS-T01.** Probe and stage a profile requiring unsupported control; launch does not occur.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
