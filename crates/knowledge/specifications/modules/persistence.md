# Transactional graph durability

**ZIP-KNOWLEDGE-PERSISTENCE-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/persistence.rs`

## Required implementation behavior

Write nodes/edges, evidence and generation metadata together, verify snapshot refs and reconcile crash. Prune only under approved retention.

## Acceptance

**ZIP-KNOWLEDGE-PERSISTENCE-T01.** Failed publish leaves no dangling active edge.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
