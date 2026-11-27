# Compilation boundary

**ZIP-COMPILATION-LIB-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/lib.rs`

## Required implementation behavior

Expose compiler, build requests and verified artifacts; inject toolchain and sandbox. Import starts no build.

## Acceptance

**ZIP-COMPILATION-LIB-T01.** Library-only consumer performs no process or network effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
