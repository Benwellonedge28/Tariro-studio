# Protocol adapter facade

**ZIP-INTEROPERABILITY-LIB-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/lib.rs`

## Required implementation behavior

Expose versioned negotiation and typed protocol ports. Connecting a remote server requires explicit launch and authority.

## Acceptance

**ZIP-INTEROPERABILITY-LIB-T01.** Import does not start a listener or contact provider.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
