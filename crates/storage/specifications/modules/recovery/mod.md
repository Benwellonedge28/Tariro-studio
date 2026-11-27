# Recovery stage boundary

**ZIP-STORAGE-RECOVERY-MOD-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/recovery/mod.rs`

## Required implementation behavior

Expose journal and reconciliation only after compatible metadata open. Recovery owns no user-facing filesystem access outside the affected store.

## Acceptance

**ZIP-STORAGE-RECOVERY-MOD-T01.** Startup never auto-reinitializes a corrupt store.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
