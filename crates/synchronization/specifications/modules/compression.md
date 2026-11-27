# Bounded compression codec

**ZIP-SYNCHRONIZATION-COMPRESSION-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/compression.rs`

## Required implementation behavior

Negotiate qualified algorithm/version, bound compressed and expanded bytes and verify digest after decode. Reject unexpected tails.

## Acceptance

**ZIP-SYNCHRONIZATION-COMPRESSION-T01.** Expansion exceeding admitted capacity cannot allocate beyond it.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
