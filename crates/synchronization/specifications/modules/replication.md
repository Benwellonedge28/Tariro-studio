# Scope-filtered bounded replication

**ZIP-SYNCHRONIZATION-REPLICATION-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/replication.rs`

## Required implementation behavior

Authorize peer and exact mutation set; stage verified data before durable apply. Enforce replay fencing and separate per-peer evidence.

## Acceptance

**ZIP-SYNCHRONIZATION-REPLICATION-T01.** Unauthorized data class does not enter transfer stream.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
