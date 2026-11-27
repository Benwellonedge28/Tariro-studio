# Security error vocabulary

**ZIP-SECURITY-ERROR-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/error.rs`

## Required implementation behavior

Distinguish unauthenticated, denied, revoked, expired, key unavailable, integrity mismatch and unsupported control. Omit unauthorized target existence and raw values.

## Acceptance

**ZIP-SECURITY-ERROR-T01.** Failure on absent and concealed resource has the same public denial.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
