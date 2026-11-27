# Scoped work transfer

**ZIP-ORCHESTRATION-DELEGATION-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/delegation.rs`

## Required implementation behavior

Bind child task and deadline to current parent grant and scoped capability. Require live lineage, no cycles and exact parent reference.

## Acceptance

**ZIP-ORCHESTRATION-DELEGATION-T01.** Child cannot schedule beyond parent ceiling or revoked state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
