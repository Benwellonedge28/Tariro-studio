# Agent actor binding

**ZIP-AGENTS-IDENTITY-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/identity.rs`

## Required implementation behavior

Use scoped authenticated agent principal and owner lineage verified by identity service. Do not accept agent-provided claims as proof.

## Acceptance

**ZIP-AGENTS-IDENTITY-T01.** Forged role text does not elevate authority.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
