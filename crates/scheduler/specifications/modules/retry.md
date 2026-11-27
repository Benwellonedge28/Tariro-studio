# Bounded retry decision

**ZIP-SCHEDULER-RETRY-001 · v1.0 · Owner:** Scheduler maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/scheduler/src/retry.rs`

## Required implementation behavior

Check typed failure and durable effect ledger before retry; charge remaining attempts, apply configured jitter and clip to deadline. Ambiguous effects wait for reconciliation.

## Acceptance

**ZIP-SCHEDULER-RETRY-T01.** No retry occurs for lost mutation response while state is unknown.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
