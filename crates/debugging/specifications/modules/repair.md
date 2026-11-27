# Scoped proposed repair

**ZIP-DEBUGGING-REPAIR-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/repair.rs`

## Required implementation behavior

Bind patch proposal to reproduced failure, exact candidate revision and allowed paths. No automatic mutation or publication.

## Acceptance

**ZIP-DEBUGGING-REPAIR-T01.** Repair touching unapproved path fails scope.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
