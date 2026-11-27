# Profile resource DTOs

**ZIP-RESOURCES-PROFILES-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/profiles.rs`

## Required implementation behavior

Expose selected preferences and explicit caps independently of observed physical capacity. Resolve derivation keys to finite measured ratios at admission. No host label selects permissions.

## Acceptance

**ZIP-RESOURCES-PROFILES-T01.** Changing hardware alters derived capacity while fixed profile preferences stay the same.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
