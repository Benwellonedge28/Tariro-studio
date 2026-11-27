# Immutable build execution

**ZIP-COMPILATION-BUILD-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/build.rs`

## Required implementation behavior

Bind snapshot, target, flags, dependencies, relevant environment and lease, stage outputs, invoke sandbox and seal only verified successful artifacts.

## Acceptance

**ZIP-COMPILATION-BUILD-T01.** Failed build leaves no cacheable result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
