# Immutable model identity

**ZIP-MODELS-IDENTIFIER-001 · v1.0 · Owner:** Models maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/models/src/identifier.rs`

## Required implementation behavior

Normalize provider, name, revision and content digest as typed identity. Alias resolution returns pinned immutable revision.

## Acceptance

**ZIP-MODELS-IDENTIFIER-T01.** Moving alias cannot replace weight digest of running assignment.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
