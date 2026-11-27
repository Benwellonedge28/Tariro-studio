# Build failure taxonomy

**ZIP-COMPILATION-ERROR-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/error.rs`

## Required implementation behavior

Distinguish missing toolchain, unsupported target, policy denial, nonzero exit, timeout, output exhaustion and incomplete artifacts.

## Acceptance

**ZIP-COMPILATION-ERROR-T01.** Compiler exit failure is never reported as cache success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
