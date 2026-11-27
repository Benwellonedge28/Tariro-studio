# Knowledge graph boundary

**ZIP-KNOWLEDGE-LIB-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/lib.rs`

## Required implementation behavior

Expose scoped graph, ingestion and read ports; inject persistence and scope validation. Linking makes no store changes.

## Acceptance

**ZIP-KNOWLEDGE-LIB-T01.** Facade can resolve types without loading graph.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
