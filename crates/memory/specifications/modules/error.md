# Memory failure classes

**ZIP-MEMORY-ERROR-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/error.rs`

## Required implementation behavior

Distinguish denied scope, stale generation, quota, expired, invalid envelope, corruption and uncertain purge.

## Acceptance

**ZIP-MEMORY-ERROR-T01.** Unauthorized lookup conceals whether a record exists.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
