# Authenticated data protection

**ZIP-SECURITY-CRYPTOGRAPHY-ENCRYPTION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/cryptography/encryption.rs`

## Required implementation behavior

Use qualified AEAD with unique nonce for each key, bind domain/version/object identity as associated data and require verification before releasing plaintext.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-ENCRYPTION-T01.** Wrong workspace, truncated ciphertext and modified header fail without plaintext.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
