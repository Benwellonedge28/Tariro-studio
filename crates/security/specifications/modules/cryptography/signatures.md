# Domain-bound signature verification

**ZIP-SECURITY-CRYPTOGRAPHY-SIGNATURES-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/cryptography/signatures.rs`

## Required implementation behavior

Verify canonical signed bytes, declared version, trusted key, algorithm and expected domain. Signature trust is independent of data scope authority.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-SIGNATURES-T01.** A valid signature for another domain cannot authorize this package.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
