# Ownership of budget mutation

**ZIP-RESOURCES-ALLOCATION-MOD-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/allocation/mod.rs`

## Required implementation behavior

Expose allocator, reservation, quota and lease types. Only allocator's transactional mutation changes active pool accounting. Read snapshots carry versions.

## Acceptance

**ZIP-RESOURCES-ALLOCATION-MOD-T01.** Compilation fixture cannot call internal reservation mutations directly.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
