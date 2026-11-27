# Workflow failure vocabulary

**ZIP-WORKFLOWS-ERROR-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/error.rs`

## Required implementation behavior

Classify invalid syntax, unknown version, cycle, expansion limit, denied step, timeout, stale checkpoint, missing artifact and unresolved effect.

## Acceptance

**ZIP-WORKFLOWS-ERROR-T01.** Loop limit rejection occurs before any task dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
