# Fenced remote restart recovery

**ZIP-DISTRIBUTED-RECOVERY-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/recovery.rs`

## Required implementation behavior

Inspect durable leases/checkpoints and exact remote effects, authorize retries only on reconciled state, preserve unresolved cleanup.

## Acceptance

**ZIP-DISTRIBUTED-RECOVERY-T01.** Owner crash around dispatch cannot yield duplicate task publication.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
