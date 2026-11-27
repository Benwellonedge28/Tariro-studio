# Qualified entropy abstraction

**ZIP-SECURITY-CRYPTOGRAPHY-RANDOM-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/cryptography/random.rs`

## Required implementation behavior

Accept injected OS-backed cryptographic source for production; fail if unavailable. Deterministic sources require test-only construction and cannot supply production keys/nonces.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-RANDOM-T01.** An entropy failure has no fallback to time or predictable data.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
