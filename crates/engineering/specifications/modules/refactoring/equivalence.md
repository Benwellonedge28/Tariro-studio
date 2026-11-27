# Equivalence evidence

**ZIP-ENGINEERING-REFACTORING-EQUIVALENCE-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/refactoring/equivalence.rs`

## Required implementation behavior

Compare declared externally observable behavior under pinned fixtures and approved tolerances. Unknown behavior remains blocked.

## Acceptance

**ZIP-ENGINEERING-REFACTORING-EQUIVALENCE-T01.** Passing small fixture cannot prove unrestricted equivalence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
