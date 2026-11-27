# Bounded network retry policy

**ZIP-NETWORKING-RETRY-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/retry.rs`

## Required implementation behavior

Retry only qualified safe reads or proven-absent idempotent writes. Respect configured attempts, server delay and remaining deadline.

## Acceptance

**ZIP-NETWORKING-RETRY-T01.** HTTP timeout after write dispatch routes to reconciliation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
