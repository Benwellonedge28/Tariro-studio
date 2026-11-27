# Target capability validation

**ZIP-COMPILATION-TARGET-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/target.rs`

## Required implementation behavior

Resolve triple, ABI, features and backend support. Unknown target or unqualified ABI denies before spawn.

## Acceptance

**ZIP-COMPILATION-TARGET-T01.** Target change recomputes admission and cache identity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
