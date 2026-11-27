# Explicit authentication adapter

**ZIP-SDK-AUTHENTICATION-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/authentication.rs`

## Required implementation behavior

Resolve qualified credential for audience and scope only within selected client transport, keep raw secrets out of logs/state.

## Acceptance

**ZIP-SDK-AUTHENTICATION-T01.** Client config and errors contain no bundled or raw tokens.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
