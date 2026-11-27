# Scoped encrypted transport payload

**ZIP-SYNCHRONIZATION-ENCRYPTION-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/encryption.rs`

## Required implementation behavior

Use qualified authenticated encryption with audience, scope, version and manifest digest as context; resolve keys only inside approved adapter.

## Acceptance

**ZIP-SYNCHRONIZATION-ENCRYPTION-T01.** Wrong scope or tampered ciphertext cannot expose plaintext.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
