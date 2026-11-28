# Stable authenticated principal

**ZIP-IDENTITY-PRINCIPAL-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/principal.rs`

## Boundary and inputs

Represent a stable principal with typed identifier and kind, trusted issuer binding and active status generation. Compute an authenticated context only from verified proof, scoped membership and trusted epoch observations. Store prepared user, agent, service and device profiles separately from verified authentication evidence.

## Behavior and failure handling

Validate kind and issuer before constructing proof-bearing context. Returned identifiers have scoped immutable views and can never be reinterpreted by a consumer as another principal kind. A raw persisted principal record or imported DTO supplies no trust. Retired principals retain provenance and fail current authorization checks.

## Acceptance

**ZIP-IDENTITY-PRINCIPAL-T01.** Attempt to deserialize an agent claim as a user and replay a retired principal record. Both fail verified context construction. A genuine in-scope proof yields only its original typed kind.
