# Pinned toolchain resolution

**ZIP-COMPILATION-TOOLCHAIN-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/toolchain.rs`

## Required implementation behavior

Resolve exact executable, version/integrity, target capabilities and qualified source. No implicit tool downloads.

## Acceptance

**ZIP-COMPILATION-TOOLCHAIN-T01.** Changing compiler identity invalidates previous build key.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
