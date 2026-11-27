# Definition version compatibility

**ZIP-WORKFLOWS-VERSIONING-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/versioning.rs`

## Required implementation behavior

Pin declared schema, workflow revision and compile digest in stored plans; refuse implicit graph changes on resume.

## Acceptance

**ZIP-WORKFLOWS-VERSIONING-T01.** Modified definition cannot reuse old checkpoints.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
