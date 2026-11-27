# Typed graph relationship

**ZIP-KNOWLEDGE-RELATIONSHIP-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/relationship.rs`

## Required implementation behavior

Bind relation kind, source/target IDs, scope, valid version and evidence/confidence. Both endpoints must authorize edge exposure.

## Acceptance

**ZIP-KNOWLEDGE-RELATIONSHIP-T01.** A private endpoint hides the edge from unauthorized traversal.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
