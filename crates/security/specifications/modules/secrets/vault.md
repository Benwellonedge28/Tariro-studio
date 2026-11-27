# Effect-local secret resolution

**ZIP-SECURITY-SECRETS-VAULT-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/secrets/vault.rs`

## Required implementation behavior

Resolve opaque reference only for authorized adapter, destination, use and epoch. Hand off minimal lifetime/scope and ensure owned buffer cleanup.

## Acceptance

**ZIP-SECURITY-SECRETS-VAULT-T01.** Wrong destination cannot read credential; borrowed value cannot escape into evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
