# Validated runtime wiring

**ZIP-RUNTIME-BUILDER-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/builder.rs`

## Required implementation behavior

Construct only from bounded queue policy, resource and storage ports, executor and stable clock. Validate availability of required cancellation/isolation controls before returning a runnable runtime.

## Acceptance

**ZIP-RUNTIME-BUILDER-T01.** Missing cleanup control prevents startup; no worker starts during builder validation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
