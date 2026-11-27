# Verification before plugin activation

**ZIP-PLUGINS-LOADER-001 · v1.0 · Owner:** Plugins maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/plugins/src/loader.rs`

## Required implementation behavior

Validate exact package digest, signer, compatibility, policy and sandbox before instantiating. Stage privately and preserve current version on failure.

## Acceptance

**ZIP-PLUGINS-LOADER-T01.** Tampered package never activates.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
