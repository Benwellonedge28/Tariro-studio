# Canonical tamper-evident chain

**ZIP-AUDIT-HASH-CHAIN-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/hash_chain.rs`

## Required implementation behavior

Hash domain/version, prior digest and validated canonical record bytes. Chain genesis uses declared representation. Ordering is sequence-based.

## Acceptance

**ZIP-AUDIT-HASH-CHAIN-T01.** Mutating or reordering one stored record breaks verification at the first affected point.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
