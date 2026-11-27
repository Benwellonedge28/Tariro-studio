# Per-chunk and final artifact integrity

**ZIP-SYNCHRONIZATION-INTEGRITY-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/integrity.rs`

## Required implementation behavior

Check sequence, length and digest for each numbered chunk and exact completed artifact digest before publish.

## Acceptance

**ZIP-SYNCHRONIZATION-INTEGRITY-T01.** Valid chunks in wrong order fail final verification.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
