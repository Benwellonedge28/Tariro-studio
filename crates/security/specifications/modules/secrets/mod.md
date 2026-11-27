# Opaque secret-reference boundary

**ZIP-SECURITY-SECRETS-MOD-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/secrets/mod.rs`

## Required implementation behavior

Expose reference, vault and rotation contracts; no display/serialization of secret bytes through public DTOs.

## Acceptance

**ZIP-SECURITY-SECRETS-MOD-T01.** A secret reference can appear in safe redacted state without revealing its value.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
