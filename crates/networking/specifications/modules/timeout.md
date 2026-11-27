# Effective monotonic deadline

**ZIP-NETWORKING-TIMEOUT-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/timeout.rs`

## Required implementation behavior

Take the earliest operation, configured networking deadline and lease deadline. Budget DNS, connect, handshake, body and flush together.

## Acceptance

**ZIP-NETWORKING-TIMEOUT-T01.** A sequence of successful phases cannot extend the original deadline.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
