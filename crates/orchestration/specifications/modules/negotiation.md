# Proposal compatibility review

**ZIP-ORCHESTRATION-NEGOTIATION-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/negotiation.rs`

## Required implementation behavior

Exchange normalized typed proposals and constraints, preserving identities and conflicts. Accept compatibility only if shared cap and preconditions agree.

## Acceptance

**ZIP-ORCHESTRATION-NEGOTIATION-T01.** Incompatible budget assumptions become explicit blocker.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
