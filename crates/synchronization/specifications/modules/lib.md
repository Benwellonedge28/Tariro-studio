# Synced state boundary

**ZIP-SYNCHRONIZATION-LIB-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/lib.rs`

## Required implementation behavior

Expose manifests, replication and checkpoint ports; inject storage and transport. Offline use requires no background connection.

## Acceptance

**ZIP-SYNCHRONIZATION-LIB-T01.** Loading sync library starts no automatic sharing.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
