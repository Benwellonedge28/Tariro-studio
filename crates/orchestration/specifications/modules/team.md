# Bounded team definition

**ZIP-ORCHESTRATION-TEAM-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/team.rs`

## Required implementation behavior

Represent membership, roles, dependencies, review independence and approved limits. Reject contradictory responsibility or scope mismatch.

## Acceptance

**ZIP-ORCHESTRATION-TEAM-T01.** Author assigned as mandatory independent reviewer causes planning failure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
