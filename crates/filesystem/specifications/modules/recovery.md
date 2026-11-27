# Filesystem intent reconciliation

**ZIP-FILESYSTEM-RECOVERY-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/recovery.rs`

## Required implementation behavior

Compare staged intent and recorded identities to live target. Confirm exact match, confirmed absence, conflict or unknown. Retry only on proven absence with live authorization.

## Acceptance

**ZIP-FILESYSTEM-RECOVERY-T01.** Lost rename reply does not trigger a duplicate blind replace.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
