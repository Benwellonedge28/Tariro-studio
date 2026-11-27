# Intelligence service boundary

**ZIP-INTELLIGENCE-LIB-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/lib.rs`

## Required implementation behavior

Expose request/response, routing, accounting and provider abstractions; no implicit adapter startup or network.

## Acceptance

**ZIP-INTELLIGENCE-LIB-T01.** Creating a local interface without a provider has no external effects.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
