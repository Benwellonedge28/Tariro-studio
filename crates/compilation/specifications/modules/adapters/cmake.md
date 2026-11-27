# CMake build adapter

**ZIP-COMPILATION-ADAPTERS-CMAKE-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/cmake.rs`

## Required implementation behavior

Stage isolated build directory and pin generator/toolchain/configure arguments. Capture configure and build results separately.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-CMAKE-T01.** Failed configure prevents build and cache promotion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
