# Service identity

**ZIP-IDENTITY-SERVICE-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/service.rs`

## Required implementation behavior

Bind issuer, service ID, audience and permitted capability family; reject interactive-user substitution. Rotate reference without widening scope.

## Acceptance

**ZIP-IDENTITY-SERVICE-T01.** Rotating an adapter credential preserves service identity and revokes its old generation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
