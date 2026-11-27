# Opt-in provider configuration

**ZIP-PROVIDERS-MANIFEST-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/manifest.rs`

## Required implementation behavior

Pin capability and endpoint metadata, admitted limits and opaque credential refs. Reject unknown required fields and unqualified overrides.

## Acceptance

**ZIP-PROVIDERS-MANIFEST-T01.** Manifest with raw credential is rejected.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
