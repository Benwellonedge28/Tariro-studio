# Validated patch application

**ZIP-ENGINEERING-IMPLEMENTATION-PATCHING-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/implementation/patching.rs`

## Required implementation behavior

Parse bounded typed patch, validate old/new paths, modes and provenance, stage isolated diff and reject partial mismatched application.

## Acceptance

**ZIP-ENGINEERING-IMPLEMENTATION-PATCHING-T01.** Rename across unauthorized boundary fails atomically.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
