# Bounded active-worker registry

**ZIP-RUNTIME-EXECUTION-WORKER-POOL-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/execution/worker_pool.rs`

## Required implementation behavior

Start workers only after admission. Track active attempts and waiters under configured slot policy and finite queue; close intake before drain. Return pressure status when full.

## Acceptance

**ZIP-RUNTIME-EXECUTION-WORKER-POOL-T01.** Full pool blocks/rejects deterministically and shutdown wakes waiting producers.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
