# Sandbox network restrictions

**ZIP-SANDBOX-NETWORK-001 · v1.0 · Owner:** Sandbox maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sandbox/src/network.rs`

## Required implementation behavior

Install network restrictions before spawn and retain deny-by-default. Apply destination controls only if backend can enforce and report them.

## Acceptance

**ZIP-SANDBOX-NETWORK-T01.** Offline sandbox produces no network requests and denies unsupported filters.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
