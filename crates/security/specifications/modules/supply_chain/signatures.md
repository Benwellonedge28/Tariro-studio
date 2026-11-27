# Package signature policy

**ZIP-SECURITY-SUPPLY-CHAIN-SIGNATURES-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/supply_chain/signatures.rs`

## Required implementation behavior

Validate artifact domain, trusted signer and approved key state with qualified verifier. Require provenance digest binding and no fallback to unsigned.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-SIGNATURES-T01.** Valid signature from untrusted issuer fails policy.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
