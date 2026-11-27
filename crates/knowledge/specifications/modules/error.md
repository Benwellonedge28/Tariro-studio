# Knowledge failure classes

**ZIP-KNOWLEDGE-ERROR-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/error.rs`

## Required implementation behavior

Distinguish invalid entity, unsupported relation, denied scope, stale revision, budget, conflict and incomplete provenance.

## Acceptance

**ZIP-KNOWLEDGE-ERROR-T01.** Denied lookup leaks neither degree nor private endpoint identity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
