# Stable provider identity

**ZIP-PROVIDERS-PROVIDER-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/provider.rs`

## Required implementation behavior

Bind name, qualified adapter/version, endpoint fingerprint, scope and advertised qualified capabilities. Endpoint change requires revalidation.

## Acceptance

**ZIP-PROVIDERS-PROVIDER-T01.** Reused name cannot inherit old credentials or scope.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
