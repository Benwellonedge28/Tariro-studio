# Budgeted retry classification

**ZIP-RUNTIME-RECOVERY-RETRY-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/recovery/retry.rs`

## Required implementation behavior

Classify failure explicitly as definitive transient, permanent or effect-unknown. Only transient safe requests consume a retry. Use configured remaining attempts and delay clipped to task deadline.

## Acceptance

**ZIP-RUNTIME-RECOVERY-RETRY-T01.** Remote timeout with uncertain mutation never follows the generic retry branch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
