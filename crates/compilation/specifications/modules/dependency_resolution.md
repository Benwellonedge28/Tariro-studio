# Approved dependency materialization

**ZIP-COMPILATION-DEPENDENCY-RESOLUTION-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/dependency_resolution.rs`

## Required implementation behavior

Use locked source manifest and approved cache. Network requires exact egress and artifact rules; report unavailable inputs separately.

## Acceptance

**ZIP-COMPILATION-DEPENDENCY-RESOLUTION-T01.** Offline missing dependency fails before automatic fetch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
