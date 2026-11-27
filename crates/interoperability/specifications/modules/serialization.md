# Bounded canonical encoding

**ZIP-INTEROPERABILITY-SERIALIZATION-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/serialization.rs`

## Required implementation behavior

Validate schema, units and byte/depth quota before decoding, preserve IDs/digests and reject duplicate mandatory keys.

## Acceptance

**ZIP-INTEROPERABILITY-SERIALIZATION-T01.** Oversized or duplicate-key input fails before downstream invocation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
