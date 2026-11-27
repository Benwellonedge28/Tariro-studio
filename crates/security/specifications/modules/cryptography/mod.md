# Versioned cryptographic ports

**ZIP-SECURITY-CRYPTOGRAPHY-MOD-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/cryptography/mod.rs`

## Required implementation behavior

Expose tagged algorithm declarations, opaque keys and qualified primitives. Disallow caller-selected unsupported schemes and implicit downgrade.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-MOD-T01.** Unknown algorithm returns typed unsupported result before key lookup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
