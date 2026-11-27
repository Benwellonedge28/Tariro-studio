# Deterministic in-memory backend

**ZIP-STORAGE-BACKENDS-MEMORY-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backends/memory.rs`

## Required implementation behavior

Maintain immutable generations and one writer; commit validates revision and swaps complete state. Advertise no disk durability and refuse production persistence capability.

## Acceptance

**ZIP-STORAGE-BACKENDS-MEMORY-T01.** Snapshot stays stable concurrent with commit. Crash durability gate rejects this backend.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
