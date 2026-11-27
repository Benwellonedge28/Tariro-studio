# Reviewed plugin update and rollback

**ZIP-PLUGINS-UPDATES-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/updates.rs`

## Required implementation behavior

Stage candidate, verify compatibility/signature and scope, activate with revision guard and retain compatible approved prior version.

## Acceptance

**ZIP-PLUGINS-UPDATES-T01.** Failed update preserves active qualified version and evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
