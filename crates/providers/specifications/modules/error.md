# Provider error taxonomy

**ZIP-PROVIDERS-ERROR-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/error.rs`

## Required implementation behavior

Keep upstream class and typed redacted status, separating unavailable, unauthorized, unsupported, rate limited and unknown mutation.

## Acceptance

**ZIP-PROVIDERS-ERROR-T01.** Rate limiting does not turn a capability into unsupported.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
