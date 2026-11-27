# Defensive bounded fuzz fixtures

**ZIP-TESTING-FUZZING-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/fuzzing.rs`

## Required implementation behavior

Run authorized local parser/boundary fixtures from synthetic corpus under finite time and memory with sanitizer evidence where supported. Keep crash report scoped.

## Acceptance

**ZIP-TESTING-FUZZING-T01.** Budget exhaustion is incomplete and observed crash retains reproducer evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
