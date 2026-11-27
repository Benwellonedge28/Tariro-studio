# Durable pending operation log

**ZIP-STORAGE-RECOVERY-JOURNAL-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/recovery/journal.rs`

## Required implementation behavior

Persist intent ID, target revision, staged artifact refs and phase before externally visible transition. Enforce allowed phase edges and monotonic sequence. Unknown outcomes stay pending.

## Acceptance

**ZIP-STORAGE-RECOVERY-JOURNAL-T01.** Crash after intent record preserves enough identity to distinguish commit from missing effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
