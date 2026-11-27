# Authorized purge and reconciliation

**ZIP-MEMORY-FORGETTING-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/forgetting.rs`

## Required implementation behavior

Authorize exact scope, tombstone eligible records, invalidate indexes/caches and reconcile replicas under policy. Keep durable deletion state and blockers.

## Acceptance

**ZIP-MEMORY-FORGETTING-T01.** Crash halfway cannot restore tombstoned results.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
