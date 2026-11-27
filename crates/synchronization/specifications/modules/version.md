# Version and cursor semantics

**ZIP-SYNCHRONIZATION-VERSION-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/version.rs`

## Required implementation behavior

Track source generation and exact applied progression. Unknown major is unavailable and stale cursor requests cannot replace current state.

## Acceptance

**ZIP-SYNCHRONIZATION-VERSION-T01.** Resume after interrupted transfer uses last committed cursor.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
