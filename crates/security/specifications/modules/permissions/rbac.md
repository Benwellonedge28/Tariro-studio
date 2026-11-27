# Scoped role eligibility

**ZIP-SECURITY-PERMISSIONS-RBAC-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/permissions/rbac.rs`

## Required implementation behavior

Resolve assigned roles to candidate effects in explicit workspace and publish effective version. Role eligibility is only one guard.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-RBAC-T01.** Maintainer in workspace A lacks implied authority in B.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
