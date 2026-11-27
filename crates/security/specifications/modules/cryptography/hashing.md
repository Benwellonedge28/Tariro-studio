# Streaming digest verification

**ZIP-SECURITY-CRYPTOGRAPHY-HASHING-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/cryptography/hashing.rs`

## Required implementation behavior

Hash bounded byte stream under qualified adapter, use typed algorithm and compare expected length and digest. Hash value is an integrity reference, not approval.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-HASHING-T01.** Corrupted or truncated content fails and supplies no verified handle.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
