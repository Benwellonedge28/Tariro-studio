# Memory origin and confidence

**ZIP-MEMORY-PROVENANCE-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/provenance.rs`

## Required implementation behavior

Bind observation/summary to immutable evidence and transform versions. Distinguish generated claim from observed fact.

## Acceptance

**ZIP-MEMORY-PROVENANCE-T01.** Summary cannot certify its own factual provenance.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
