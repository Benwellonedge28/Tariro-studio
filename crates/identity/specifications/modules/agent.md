# Agent principal representation

**ZIP-IDENTITY-AGENT-001 · v1.0 · Owner:** Identity maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/identity/src/agent.rs`

## Required implementation behavior

Bind agent ID to assignment, owner lineage and revocation epoch. Agent can present only delegated scope and cannot authorize its own delegation.

## Acceptance

**ZIP-IDENTITY-AGENT-T01.** An agent in one assignment cannot act in another with the same model.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
