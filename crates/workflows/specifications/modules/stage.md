# Stage boundary and evidence

**ZIP-WORKFLOWS-STAGE-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/stage.rs`

## Required implementation behavior

Bind stage ID, prerequisite set, required gates, allowed steps and artifacts. Advance stage only after mandatory checks verify exact outputs.

## Acceptance

**ZIP-WORKFLOWS-STAGE-T01.** One incomplete check holds stage after process exit.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
