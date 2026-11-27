# Revision-bound document edit

**ZIP-DOCUMENTATION-EDITING-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/editing.rs`

## Required implementation behavior

Validate target path, expected blob and retained source/provenance, create scoped diff, preserve unrelated modifications. Refuse a conflict rather than guessing.

## Acceptance

**ZIP-DOCUMENTATION-EDITING-T01.** Concurrent edit rejects without overwriting reviewer change.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
