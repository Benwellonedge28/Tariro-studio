# Attenuated scope inheritance

**ZIP-SECURITY-PERMISSIONS-INHERITANCE-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/permissions/inheritance.rs`

## Required implementation behavior

Intersect ancestor grants, scopes, ceilings and time; preserve explicit denies and provenance. Reject cycles or malformed lineage.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-INHERITANCE-T01.** Nested role cannot expand a denied path or raise parent quota.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
