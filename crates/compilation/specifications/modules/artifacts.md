# Artifact integrity and scope

**ZIP-COMPILATION-ARTIFACTS-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/artifacts.rs`

## Required implementation behavior

Record output digest, mode, target and tool provenance; verify staging scope and exit before publishing artifact refs.

## Acceptance

**ZIP-COMPILATION-ARTIFACTS-T01.** Missing expected artifact blocks build completion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
