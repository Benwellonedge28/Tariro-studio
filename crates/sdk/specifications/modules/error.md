# Client error representation

**ZIP-SDK-ERROR-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/error.rs`

## Required implementation behavior

Preserve typed remote/local error, unavailable capability, unknown effect, cancellation and corrupt fixture with redacted context.

## Acceptance

**ZIP-SDK-ERROR-T01.** Timeout after dispatch remains unknown.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
