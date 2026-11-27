# Sync operation outcomes

**ZIP-SYNCHRONIZATION-ERROR-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/error.rs`

## Required implementation behavior

Distinguish incompatibility, denied peer, divergent revision, bad digest, queue full, interrupted transfer and unresolved write.

## Acceptance

**ZIP-SYNCHRONIZATION-ERROR-T01.** A conflicting replica never returns synchronized success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
