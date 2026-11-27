# Preserved divergent history

**ZIP-SYNCHRONIZATION-CONFLICT-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/conflict.rs`

## Required implementation behavior

Detect concurrent revisions and keep both approved variants plus source provenance. Require reviewed resolution policy for noncommutative changes.

## Acceptance

**ZIP-SYNCHRONIZATION-CONFLICT-T01.** Divergent records are not silently overwritten by timestamp.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
