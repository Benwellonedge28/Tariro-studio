# DAG dependency resolution

**ZIP-WORKFLOWS-DEPENDENCY-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/dependency.rs`

## Required implementation behavior

Order stable dependencies, identify cycles, mark dependent ready only after required predecessor success. Unresolved or failed predecessor blocks.

## Acceptance

**ZIP-WORKFLOWS-DEPENDENCY-T01.** Failed stage cannot start downstream step.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
