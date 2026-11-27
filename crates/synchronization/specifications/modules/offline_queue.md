# Bounded disconnected intent queue

**ZIP-SYNCHRONIZATION-OFFLINE-QUEUE-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/offline_queue.rs`

## Required implementation behavior

Store immutable intent with expiry, scope and expected base, under configured item/byte bounds. Revalidate before any delayed transmission.

## Acceptance

**ZIP-SYNCHRONIZATION-OFFLINE-QUEUE-T01.** Expired or stale queued write does not run on reconnect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
