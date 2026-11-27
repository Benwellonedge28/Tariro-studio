# Embedded durable backend

**ZIP-STORAGE-BACKENDS-REDB-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backends/redb.rs`

## Required implementation behavior

Use one qualified redb writer and versioned keyspace. Open known format read-only before obtaining write access. Transaction writes state, outbox and receipt in same durable commit. Batch and value limits enforced before calls.

## Acceptance

**ZIP-STORAGE-BACKENDS-REDB-T01.** Power-loss fixture validates before/after commit atomicity and wrong schema denies modification.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
