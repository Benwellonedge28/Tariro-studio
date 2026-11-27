# Opaque key lifecycle

**ZIP-SECURITY-CRYPTOGRAPHY-KEY-MANAGEMENT-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/cryptography/key_management.rs`

## Required implementation behavior

Track algorithm, owner, generation, usage, active/retired/revoked status and approved rotation. Keep key material within secure adapter.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-KEY-MANAGEMENT-T01.** Wrong usage or revoked key denies a new signing operation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
