# Budget-aware context reduction

**ZIP-CONTEXT-COMPRESSION-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/compression.rs`

## Required implementation behavior

Compress only eligible optional material, preserving source IDs and trust. Measure transformed window and treat transformations as unverified summaries.

## Acceptance

**ZIP-CONTEXT-COMPRESSION-T01.** Required policy is never compressed, and oversize transform fails.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
