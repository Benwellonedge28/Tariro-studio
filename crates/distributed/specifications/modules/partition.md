# Network partition behavior

**ZIP-DISTRIBUTED-PARTITION-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/partition.rs`

## Required implementation behavior

Freeze unverifiable remote promotion, mark availability uncertain and fence prior lease before authorized replacement. Maintain safe local operation.

## Acceptance

**ZIP-DISTRIBUTED-PARTITION-T01.** Healing partition cannot resurrect old epoch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
