# SDK facade

**ZIP-SDK-LIB-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/lib.rs`

## Required implementation behavior

Expose typed client/request/response helpers and scoped modules. Linking creates no provider/client credentials.

## Acceptance

**ZIP-SDK-LIB-T01.** Import changes no configuration or network state.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
