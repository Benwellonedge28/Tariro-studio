# Rooted component resolution

**ZIP-FILESYSTEM-CANONICALIZATION-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/canonicalization.rs`

## Required implementation behavior

Resolve one component at a time beneath an opened root using qualified no-follow semantics. Validate final object identity and mode rather than trusting a string prefix.

## Acceptance

**ZIP-FILESYSTEM-CANONICALIZATION-T01.** Swap an ancestor between checks and confirm no outside read/write succeeds.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
