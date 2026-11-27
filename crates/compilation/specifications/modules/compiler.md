# Supervised compiler dispatch

**ZIP-COMPILATION-COMPILER-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/compiler.rs`

## Required implementation behavior

Validate toolchain and build request, reserve resources, invoke qualified adapter and expose actual receipt after cleanup.

## Acceptance

**ZIP-COMPILATION-COMPILER-T01.** Unapproved compiler path cannot dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
