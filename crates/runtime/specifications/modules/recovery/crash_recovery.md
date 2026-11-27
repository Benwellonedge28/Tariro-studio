# Supervisor restart and fencing

**ZIP-RUNTIME-RECOVERY-CRASH-RECOVERY-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/recovery/crash_recovery.rs`

## Required implementation behavior

Find nonterminal durable states, fence expired epochs, inspect process ownership/effects, and restore matching verification artifacts. Missing mandatory guarantees block startup work.

## Acceptance

**ZIP-RUNTIME-RECOVERY-CRASH-RECOVERY-T01.** Crash after child creation before outcome does not launch second attempt until reconciled.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
