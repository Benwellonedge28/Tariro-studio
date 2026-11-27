# Dynamic proposal group

**ZIP-ORCHESTRATION-SWARM-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/swarm.rs`

## Required implementation behavior

Admit each participant under role, digest, scope and resource lease. Aggregate typed findings and report outstanding disagreements; never count votes as approval.

## Acceptance

**ZIP-ORCHESTRATION-SWARM-T01.** Swarm growth stops at effective admission budget.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
