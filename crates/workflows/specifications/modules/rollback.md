# Rollback and reconciliation

**ZIP-WORKFLOWS-ROLLBACK-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/rollback.rs`

## Required implementation behavior

Verify compatible prior state, current authority and exact target before rollback. Preserve immutable effects and report partial/unknown outcome.

## Acceptance

**ZIP-WORKFLOWS-ROLLBACK-T01.** Rollback cannot erase external receipt or silently downgrade schema.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
