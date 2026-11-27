# Distribution license gate

**ZIP-MODELS-LICENSING-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/licensing.rs`

## Required implementation behavior

Track source license evidence, version, usage restrictions and unknown state. Permit local or export only under applicable documented policy and scope.

## Acceptance

**ZIP-MODELS-LICENSING-T01.** Unknown distribution terms block export independently of file integrity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
