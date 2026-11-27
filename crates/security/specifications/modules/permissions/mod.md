# Permission decision composition

**ZIP-SECURITY-PERMISSIONS-MOD-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/permissions/mod.rs`

## Required implementation behavior

Expose RBAC, ABAC, capability, inheritance and revocation as input boundaries to one authoritative decision. Enforce deny override.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-MOD-T01.** Direct use of any one evaluator cannot authorize an external effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
