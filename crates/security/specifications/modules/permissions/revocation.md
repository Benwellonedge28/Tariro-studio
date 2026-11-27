# Revocation epoch enforcement

**ZIP-SECURITY-PERMISSIONS-REVOCATION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/permissions/revocation.rs`

## Required implementation behavior

Read current epoch at effect claim and deny old generations. Record revocation durably; reconcile already-claimed effects separately.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-REVOCATION-T01.** Restart cannot revive a revoked capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
