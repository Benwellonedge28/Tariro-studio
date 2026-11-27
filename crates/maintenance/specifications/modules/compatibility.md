# Upgrade qualification

**ZIP-MAINTENANCE-COMPATIBILITY-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/compatibility.rs`

## Required implementation behavior

Check exact producer/consumer versions, schema transition and retained rollback path. Unknown compatibility blocks promotion.

## Acceptance

**ZIP-MAINTENANCE-COMPATIBILITY-T01.** Incompatible persisted state prevents automated update.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
