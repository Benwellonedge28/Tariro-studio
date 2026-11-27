# Credential generation replacement

**ZIP-SECURITY-SECRETS-ROTATION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/secrets/rotation.rs`

## Required implementation behavior

Stage new generation, verify live scope, atomically activate reference and revoke old effect authority. Reconcile in-flight effects and retain only approved recovery handles.

## Acceptance

**ZIP-SECURITY-SECRETS-ROTATION-T01.** Partial rotation before activation leaves old generation consistent; after activation old cannot start work.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
