# Local release adapter

**ZIP-DEPLOYMENT-PROVIDERS-LOCAL-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/providers/local.rs`

## Required implementation behavior

Stage in owned root, verify digest and atomically switch only under approved local revision. Preserve prior compatible artifact per policy.

## Acceptance

**ZIP-DEPLOYMENT-PROVIDERS-LOCAL-T01.** Failed staging never replaces active artifact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
