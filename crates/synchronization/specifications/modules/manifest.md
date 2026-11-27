# Immutable transfer manifest

**ZIP-SYNCHRONIZATION-MANIFEST-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/manifest.rs`

## Required implementation behavior

Bind source/destination scope, generation, sequence, artifacts, digest algorithm, lengths and version. Validate before allocation.

## Acceptance

**ZIP-SYNCHRONIZATION-MANIFEST-T01.** Unknown schema quarantines batch without partially applying records.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
