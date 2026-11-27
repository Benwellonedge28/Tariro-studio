# Durable apply cursor

**ZIP-SYNCHRONIZATION-CHECKPOINT-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/checkpoint.rs`

## Required implementation behavior

Commit applied delta and latest cursor/idempotency state in same storage transaction. Persist unknown outcome for inspection.

## Acceptance

**ZIP-SYNCHRONIZATION-CHECKPOINT-T01.** Crash after commit before reply resumes without reapplying.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
