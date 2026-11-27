# Worker proof and audience

**ZIP-DISTRIBUTED-IDENTITY-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/identity.rs`

## Required implementation behavior

Verify qualified peer identity, nonce or channel binding, expiry and task-specific audience before using advertised status.

## Acceptance

**ZIP-DISTRIBUTED-IDENTITY-T01.** Another worker cannot reuse a task acceptance proof.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
