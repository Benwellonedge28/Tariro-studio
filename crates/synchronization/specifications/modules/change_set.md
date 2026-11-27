# Ordered scoped delta

**ZIP-SYNCHRONIZATION-CHANGE-SET-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/change_set.rs`

## Required implementation behavior

Normalize and validate unique operations, source base and evidence. Any denied path or unsupported delete blocks apply instead of dropping operation.

## Acceptance

**ZIP-SYNCHRONIZATION-CHANGE-SET-T01.** Duplicate record ID with different payload conflicts.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
