# Transport failure vocabulary

**ZIP-NETWORKING-ERROR-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/error.rs`

## Required implementation behavior

Separate denied destination, offline, resolution, TLS, timeout, response truncation, rate limit and unknown effect. Redact credentials and unsafe destinations.

## Acceptance

**ZIP-NETWORKING-ERROR-T01.** Lost mutation response remains unknown, never assumed absent.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
