# Threat and control registry

**ZIP-SECURITY-THREAT-MODEL-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/threat_model.rs`

## Required implementation behavior

Bind threat, asset, actor, trust crossing, invariant, residual risk and linked qualification evidence per effect. Record unavailable controls explicitly.

## Acceptance

**ZIP-SECURITY-THREAT-MODEL-T01.** Missing mandatory mitigation blocks affected capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
