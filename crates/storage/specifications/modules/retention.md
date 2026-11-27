# Pinned generation protection

**ZIP-STORAGE-RETENTION-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/retention.rs`

## Required implementation behavior

plan_prune(cutoff: Timestamp, view: ReferenceSnapshot) -> Result<PrunePlan, StorageError>. Filter retained/pinned/reachable objects first. Recheck generation and references before delete; partial deletion yields per-item cleanup receipt.

## Acceptance

**ZIP-STORAGE-RETENTION-T01.** An object pinned after plan is not deleted; expired unreferenced object is collected only after configured grace.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
