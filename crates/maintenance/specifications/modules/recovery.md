# Resumable maintenance recovery

**ZIP-MAINTENANCE-RECOVERY-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/recovery.rs`

## Required implementation behavior

Read durable intents, verify target revision and backup integrity, reconcile partial or uncertain updates and pause on unresolved conflicts.

## Acceptance

**ZIP-MAINTENANCE-RECOVERY-T01.** Restart after interrupted update resumes or restores without overwriting valid state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
