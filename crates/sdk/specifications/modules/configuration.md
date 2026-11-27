# Validated client configuration

**ZIP-SDK-CONFIGURATION-001 · v1.0 · Owner:** Sdk maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/sdk/src/configuration.rs`

## Required implementation behavior

Load bounded typed endpoint/profile schemas and opaque credential refs, reject unsafe fallback and unknown keys.

## Acceptance

**ZIP-SDK-CONFIGURATION-T01.** Invalid endpoint cannot become default remote route.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
