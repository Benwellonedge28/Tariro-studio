# Canonical protocol envelope

**ZIP-INTEROPERABILITY-PROTOCOL-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/protocol.rs`

## Required implementation behavior

Pin request ID, protocol version, capability, scope, data classification and typed payload. Reject missing required fields before effects.

## Acceptance

**ZIP-INTEROPERABILITY-PROTOCOL-T01.** Unknown mandatory field fails schema.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
