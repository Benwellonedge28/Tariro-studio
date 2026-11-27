# Versioned baseline defaults

**ZIP-CONFIGURATION-DEFAULTS-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/defaults.rs`

## Required implementation behavior

load_defaults(manifest: VerifiedDefaults, registry: &KeyRegistry) -> Result<DefaultLayer, ConfigError>. Check schema/version and integrity, then validate every required key exactly once. Apply no fallback literals on a missing key.

## Acceptance

**ZIP-CONFIGURATION-DEFAULTS-T01.** Remove one mandatory limit and prove the runtime cannot admit work through default resolution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
