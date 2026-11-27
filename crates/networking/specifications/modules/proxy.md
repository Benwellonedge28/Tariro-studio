# Explicit approved proxy routing

**ZIP-NETWORKING-PROXY-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/proxy.rs`

## Required implementation behavior

Use configured proxy only, require independent endpoint and proxy permission, and prevent credentials from crossing unintended origins.

## Acceptance

**ZIP-NETWORKING-PROXY-T01.** Inherited proxy variables do not affect route selection.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
