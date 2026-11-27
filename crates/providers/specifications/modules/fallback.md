# Explicit compatible fallback

**ZIP-PROVIDERS-FALLBACK-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/fallback.rs`

## Required implementation behavior

Only consider pre-approved provider and data scope; classify unknown prior effect before retry; local-only never becomes remote.

## Acceptance

**ZIP-PROVIDERS-FALLBACK-T01.** Unavailable local adapter emits no outbound request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
