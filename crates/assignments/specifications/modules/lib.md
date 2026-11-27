# Assignment crate boundary

**ZIP-ASSIGNMENTS-LIB-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/lib.rs`

## Required implementation behavior

Expose validated spec, state, typed commands and receipt; composition root injects storage, policy and verification ports. No hidden threads or remote writes.

## Acceptance

**ZIP-ASSIGNMENTS-LIB-T01.** Link assignment DTOs without daemon startup.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
