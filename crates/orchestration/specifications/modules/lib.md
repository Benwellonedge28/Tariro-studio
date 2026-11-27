# Orchestration engine boundary

**ZIP-ORCHESTRATION-LIB-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/lib.rs`

## Required implementation behavior

Expose plan, coordination and verified outcome ports; inject runtime, agent and policy-holding services. No work starts on initialization.

## Acceptance

**ZIP-ORCHESTRATION-LIB-T01.** Construct without starting tasks or network connections.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
