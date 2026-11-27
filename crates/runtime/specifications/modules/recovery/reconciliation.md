# Effect receipt comparison

**ZIP-RUNTIME-RECOVERY-RECONCILIATION-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/recovery/reconciliation.rs`

## Required implementation behavior

Compare observed ref/receipt against stable intent, input digest and expected revision. Exact match completes. Definitive absence can retry under live authority. Conflict and unknown block.

## Acceptance

**ZIP-RUNTIME-RECOVERY-RECONCILIATION-T01.** Duplicate response and mismatched remote branch each produce correct durable decisions.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
