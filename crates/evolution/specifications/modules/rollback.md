# Qualified reversible promotion

**ZIP-EVOLUTION-ROLLBACK-001 · v1.0 · Owner:** Evolution maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/evolution/src/rollback.rs`

## Required implementation behavior

Require compatible previously verified state and distinct authority before rollback. Record actual effect and reconcile incomplete outcomes.

## Acceptance

**ZIP-EVOLUTION-ROLLBACK-T01.** Rollback without qualified recovery material remains blocked.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
