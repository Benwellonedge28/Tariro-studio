# Reviewed dependency update candidate

**ZIP-MAINTENANCE-DEPENDENCY-UPDATES-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/dependency_updates.rs`

## Required implementation behavior

Pin current graph and proposed revision, verify provenance, policy and compatibility, and stage diff without merging.

## Acceptance

**ZIP-MAINTENANCE-DEPENDENCY-UPDATES-T01.** Unqualified transitive change blocks proposed update.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
