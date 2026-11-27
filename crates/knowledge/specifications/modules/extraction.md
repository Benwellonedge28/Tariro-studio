# Evidence-linked fact candidates

**ZIP-KNOWLEDGE-EXTRACTION-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/extraction.rs`

## Required implementation behavior

Extract entities/relationships from approved source revision and record exact locations and confidence. Mark model observations unverified until corroborated.

## Acceptance

**ZIP-KNOWLEDGE-EXTRACTION-T01.** Unsupported claim cannot be promoted as observed edge.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
