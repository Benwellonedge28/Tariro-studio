# Stage artifact ownership

**ZIP-WORKFLOWS-ARTIFACTS-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/artifacts.rs`

## Required implementation behavior

Record digest, producer, scope and verification status. Consumers verify exact artifact identity and data class before read.

## Acceptance

**ZIP-WORKFLOWS-ARTIFACTS-T01.** Artifact from different execution cannot satisfy current step.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
