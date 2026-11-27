# Graph record validation

**ZIP-KNOWLEDGE-SCHEMA-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/schema.rs`

## Required implementation behavior

Validate schema version, kind, IDs, edge cardinality and required evidence before materializing graph. Reject unknown mandatory fields.

## Acceptance

**ZIP-KNOWLEDGE-SCHEMA-T01.** Malformed relationship cannot create a partial node.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
