# Immutable citation construction

**ZIP-RESEARCH-CITATION-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/citation.rs`

## Required implementation behavior

Bind observed URL/path, source revision, evidence span and retrieval status without leaking private data. Require actual retrieved evidence for direct citation.

## Acceptance

**ZIP-RESEARCH-CITATION-T01.** Dead link or wrong digest flagged and not treated as verified.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
