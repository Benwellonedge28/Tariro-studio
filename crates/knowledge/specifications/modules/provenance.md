# Exact fact evidence

**ZIP-KNOWLEDGE-PROVENANCE-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/provenance.rs`

## Required implementation behavior

Store immutable source path/span or object digest, extraction rule version and confidence. Surface missing or stale sources distinctly.

## Acceptance

**ZIP-KNOWLEDGE-PROVENANCE-T01.** Rewritten file invalidates old qualified fact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
