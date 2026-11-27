# Orchestration failure classes

**ZIP-ORCHESTRATION-ERROR-001 · v1.0 · Owner:** Orchestration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/orchestration/src/error.rs`

## Required implementation behavior

Classify invalid graph, conflict, no eligible route, budget exhausted, denied effect, stale outcome and escalation. No success from unresolved conflict.

## Acceptance

**ZIP-ORCHESTRATION-ERROR-T01.** Ambiguous proposal status never implies committed change.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
