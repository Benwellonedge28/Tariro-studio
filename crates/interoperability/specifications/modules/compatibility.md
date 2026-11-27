# Cross-version mapping qualification

**ZIP-INTEROPERABILITY-COMPATIBILITY-001 · v1.0 · Owner:** Interoperability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/interoperability/src/compatibility.rs`

## Required implementation behavior

Map only verified compatible operations, preserving authorization boundaries, units and failure semantics. Unknown differences stay unsupported.

## Acceptance

**ZIP-INTEROPERABILITY-COMPATIBILITY-T01.** A translation cannot broaden a read into write.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
