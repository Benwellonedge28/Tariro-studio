# Snapshot graph operations

**ZIP-KNOWLEDGE-GRAPH-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/graph.rs`

## Required implementation behavior

Stage revisioned node/edge mutations, check endpoints and provenance before activation, and expose immutable snapshot handles.

## Acceptance

**ZIP-KNOWLEDGE-GRAPH-T01.** Crash before promotion leaves previous complete graph readable.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
