# Mandatory restriction intersection

**ZIP-CONFIGURATION-OVERRIDES-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/overrides.rs`

## Required implementation behavior

merge(preferences: PreferenceLayers, policies: PolicyLayers) -> Result<TypedConfig, ConfigError>. Resolve presentation preferences by precedence. Maxima take minimum, permits intersect, requirements union, exact constraints must agree. Record contributing origins. Never treat missing allowlist as wildcard.

## Acceptance

**ZIP-CONFIGURATION-OVERRIDES-T01.** Workspace tries to widen network domain or memory ceiling; effective scope stays within higher policy.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
