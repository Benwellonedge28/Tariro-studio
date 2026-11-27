# Policy-bound memory replication

**ZIP-MEMORY-SYNCHRONIZATION-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/synchronization.rs`

## Required implementation behavior

Sync only authorized record/artifact scope and version, enforce egress and tombstones; reconcile conflicts and quota independently.

## Acceptance

**ZIP-MEMORY-SYNCHRONIZATION-T01.** A delayed replica cannot resurrect a tombstoned record.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
