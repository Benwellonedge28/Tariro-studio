# Scoped capability negotiation

**ZIP-INTEROPERABILITY-NEGOTIATION-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/negotiation.rs`

## Required implementation behavior

Intersect exact supported major/minor features, authentication and configured scope; return explicit qualified view. ULABI remains unadvertised until verified.

## Acceptance

**ZIP-INTEROPERABILITY-NEGOTIATION-T01.** Unknown major blocks without downgrade or effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
