# Scoped storage accounting

**ZIP-ECONOMICS-STORAGE-USAGE-001 · v1.0 · Owner:** Economics maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/economics/src/storage_usage.rs`

## Required implementation behavior

Count measured bytes by approved workspace and representation, distinguish reserved and physically retained bytes. Verify release.

## Acceptance

**ZIP-ECONOMICS-STORAGE-USAGE-T01.** Pinned/retained artifact does not return spendable capacity early.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
