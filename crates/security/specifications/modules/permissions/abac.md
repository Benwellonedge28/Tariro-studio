# Typed attribute predicates

**ZIP-SECURITY-PERMISSIONS-ABAC-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/permissions/abac.rs`

## Required implementation behavior

Evaluate typed actor, resource, operation and environment attributes from trusted sources. Unknown mandatory attributes deny.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-ABAC-T01.** Missing classification never satisfies a public-only predicate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
