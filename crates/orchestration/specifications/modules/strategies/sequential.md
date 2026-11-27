# Serial execution strategy

**ZIP-ORCHESTRATION-STRATEGIES-SEQUENTIAL-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/strategies/sequential.rs`

## Required implementation behavior

Propose one eligible step in stable order; count unreaped attempt as active until supervisor proves cleanup.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-SEQUENTIAL-T01.** Next step waits while prior child still holds lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
