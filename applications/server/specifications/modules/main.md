# Gateway application composition

**ZIP-SERVER-MAIN-001 · v1.0 · Owner:** Server maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/server/src/main.rs`

## Required implementation behavior

Load validated policy, runtime, listener, identity and resource ports before accepting connections. Bind loopback unless remote capability is approved and verified. Propagate startup failures.

## Acceptance

**ZIP-SERVER-MAIN-T01.** Clean local start opens no public listener and fails closed for missing mandatory auth.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
