# Process-wide lifecycle

**ZIP-RUNTIME-LIFECYCLE-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/lifecycle.rs`

## Required implementation behavior

States Created, Ready, Running, Draining, Stopped and Failed. Bind one supervisor ownership per generation. Drain blocks new intake; only verified teardown enters Stopped.

## Acceptance

**ZIP-RUNTIME-LIFECYCLE-T01.** Repeated shutdown matches stable outcome and cannot restart a terminal runtime.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
