# Typed hypothesis record

**ZIP-DEBUGGING-HYPOTHESIS-001 · v1.0 · Owner:** Debugging maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/debugging/src/hypothesis.rs`

## Required implementation behavior

Store claim, expected observable result, referenced evidence and falsification test. Keep untested status explicit.

## Acceptance

**ZIP-DEBUGGING-HYPOTHESIS-T01.** Contradictory observation invalidates candidate hypothesis.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
