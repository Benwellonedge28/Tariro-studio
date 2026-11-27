# Effect-specific capability checking

**ZIP-SECURITY-PERMISSIONS-CAPABILITY-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/permissions/capability.rs`

## Required implementation behavior

Bind opaque capability to subject, target, operation, version, expiry and lineage. Validate before dispatch and fence prior epochs.

## Acceptance

**ZIP-SECURITY-PERMISSIONS-CAPABILITY-T01.** A read capability is rejected for a write request with the same target ID.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
