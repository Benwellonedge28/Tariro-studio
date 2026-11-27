# Repair verification

**ZIP-DEBUGGING-VALIDATION-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/validation.rs`

## Required implementation behavior

Re-run approved reproduction and required regressions against exact patch digest, preserve actual old/new outcomes.

## Acceptance

**ZIP-DEBUGGING-VALIDATION-T01.** Without reproduced baseline, report qualification limit.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
