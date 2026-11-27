# Immutable context source records

**ZIP-CONTEXT-PROVENANCE-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/provenance.rs`

## Required implementation behavior

Record source revision, bytes/span, digest, trust, classification and selection status for each item. Reject stale or invalid spans before use.

## Acceptance

**ZIP-CONTEXT-PROVENANCE-T01.** Link to changed revision cannot pass exact-content verification.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
