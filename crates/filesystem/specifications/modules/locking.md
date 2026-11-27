# Ordered owned write locks

**ZIP-FILESYSTEM-LOCKING-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/locking.rs`

## Required implementation behavior

Serialize normalized scope keys in stable order. Bind lock to lease and generation. Never hold lock across unrelated I/O; release only the acquired ownership.

## Acceptance

**ZIP-FILESYSTEM-LOCKING-T01.** Two reversed lock sets produce no deadlock or partial write.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
