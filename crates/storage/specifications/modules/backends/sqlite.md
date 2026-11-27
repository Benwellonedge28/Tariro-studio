# Optional relational adapter

**ZIP-STORAGE-BACKENDS-SQLITE-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backends/sqlite.rs`

## Required implementation behavior

Map logical keys to binary values using parameterized statements. Configure one writer and qualified durability mode. Transactions stage all state/outbox/receipt writes; unavailable guarantees disable writes.

## Acceptance

**ZIP-STORAGE-BACKENDS-SQLITE-T01.** Exercise contention, rollback on constraint failure, byte-order key scans and cross-backend conformance.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
