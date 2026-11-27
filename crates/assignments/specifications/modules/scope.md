# Effect scope computation

**ZIP-ASSIGNMENTS-SCOPE-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/scope.rs`

## Required implementation behavior

Compute intersection of repository identity, pinned base, allowed effects/paths/classes and destinations. Normalize both paths for renamed files. Any missing required authority denies.

## Acceptance

**ZIP-ASSIGNMENTS-SCOPE-T01.** Allowlisted Markdown path cannot be renamed into an implementation path.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
