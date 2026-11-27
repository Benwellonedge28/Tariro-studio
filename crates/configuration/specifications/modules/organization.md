# Organization policy overlay

**ZIP-CONFIGURATION-ORGANIZATION-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/organization.rs`

## Required implementation behavior

Validate authority and revision before admitting restrictions. Normalize allowed destinations and capability sets, and apply changes atomically to future decisions.

## Acceptance

**ZIP-CONFIGURATION-ORGANIZATION-T01.** An expired or invalidly attributed policy does not relax a previous active restriction.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
