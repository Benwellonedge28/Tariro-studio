# Atomic vector allocation

**ZIP-RESOURCES-ALLOCATION-ALLOCATOR-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/allocation/allocator.rs`

## Required implementation behavior

Under one transaction or stable pool lock order check revision, policy and remaining demand for every coordinate, then add checked reservations together. Reject entire vector on any failure.

## Acceptance

**ZIP-RESOURCES-ALLOCATION-ALLOCATOR-T01.** Concurrent requests competing for two shared pools cannot partially reserve either pool.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
