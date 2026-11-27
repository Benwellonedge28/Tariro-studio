# Authoritative owner orchestration

**ZIP-DISTRIBUTED-COORDINATOR-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/coordinator.rs`

## Required implementation behavior

Maintain durable task ownership, issue/fence attempts, observe receipts and update authoritative state only under exact lease and evidence.

## Acceptance

**ZIP-DISTRIBUTED-COORDINATOR-T01.** Late remote receipt cannot advance a superseded task.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
