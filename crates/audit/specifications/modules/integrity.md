# Checkpoint and chain validation

**ZIP-AUDIT-INTEGRITY-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/integrity.rs`

## Required implementation behavior

Verify contiguous sequence, exact digests and configured signed checkpoints. Return first failed segment and immutable scope; no silent repair.

## Acceptance

**ZIP-AUDIT-INTEGRITY-T01.** Truncated suffix fails when inconsistent with recorded checkpoint.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
