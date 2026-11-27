# Versioned semantic definitions

**ZIP-KNOWLEDGE-ONTOLOGY-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/ontology.rs`

## Required implementation behavior

Define permitted node/edge kinds, domain/range and constraints, distinguishing unknown relation from invalid relation.

## Acceptance

**ZIP-KNOWLEDGE-ONTOLOGY-T01.** An undeclared kind cannot acquire confirmed semantics.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
