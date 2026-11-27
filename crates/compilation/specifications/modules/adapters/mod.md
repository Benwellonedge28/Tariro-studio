# Build adapter negotiation

**ZIP-COMPILATION-ADAPTERS-MOD-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/mod.rs`

## Required implementation behavior

Select by qualified manifest/toolchain and target capabilities. Ambiguous build system requires explicit selection.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-MOD-T01.** Unknown adapter cannot invoke generic shell.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
