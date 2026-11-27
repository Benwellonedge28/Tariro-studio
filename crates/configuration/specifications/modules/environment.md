# Explicit environment mapping

**ZIP-CONFIGURATION-ENVIRONMENT-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/environment.rs`

## Required implementation behavior

read_environment(input: &dyn Environment, allow: &EnvironmentMap) -> Result<PreferenceLayer, ConfigError>. Each approved variable maps to a single registry key with explicit parse kind. Ignore unrelated environment entries; reject duplicates and privileged mappings.

## Acceptance

**ZIP-CONFIGURATION-ENVIRONMENT-T01.** Provide an unapproved egress key and approved scalar preference; only the latter enters the candidate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
