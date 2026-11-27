# Versioned at-rest envelope

**ZIP-STORAGE-ENCRYPTION-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/encryption.rs`

## Required implementation behavior

Encryption binds schema, object identity and workspace as authenticated data; keys are opaque references from approved adapters. Persist envelope version, key ID, unique nonce and bounded ciphertext. Reject decryption/tag failure before returning any plaintext.

## Acceptance

**ZIP-STORAGE-ENCRYPTION-T01.** Modified header or cross-workspace reference fails authentication. Restart may read explicitly retained older key version.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
