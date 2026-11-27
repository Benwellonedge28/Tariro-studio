# Immutable graph generations

**ZIP-KNOWLEDGE-VERSIONING-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/versioning.rs`

## Required implementation behavior

Bind generation identity to input revision and ontology; activate with compare-and-swap and retain prior verified generation within policy.

## Acceptance

**ZIP-KNOWLEDGE-VERSIONING-T01.** Concurrent stale reindex cannot overwrite current graph.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
