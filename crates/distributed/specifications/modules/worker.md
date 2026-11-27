# Contained single task attempt

**ZIP-DISTRIBUTED-WORKER-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/worker.rs`

## Required implementation behavior

Verify owner, exact plan, lease and attempt epoch before spawn; capture actual output and teardown state. Never self-promote results.

## Acceptance

**ZIP-DISTRIBUTED-WORKER-T01.** Expired worker cannot write authoritative owner state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
