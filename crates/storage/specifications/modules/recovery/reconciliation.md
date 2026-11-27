# Storage effect recovery

**ZIP-STORAGE-RECOVERY-RECONCILIATION-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/recovery/reconciliation.rs`

## Required implementation behavior

Read receipt, selector and referenced bytes; classify completed, safely absent, conflicting or unknown. Retry only when absence and invariant checks prove idempotence. Preserve corruption for operator review.

## Acceptance

**ZIP-STORAGE-RECOVERY-RECONCILIATION-T01.** A mismatched selector and missing staged object cause a blocked verdict instead of unverified success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
