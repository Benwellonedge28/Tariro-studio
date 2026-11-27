# Immutable deployable artifact

**ZIP-DEPLOYMENT-ARTIFACT-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/artifact.rs`

## Required implementation behavior

Pin package digest, build provenance, supported platform and signed manifest. Verify contents before passing to staging.

## Acceptance

**ZIP-DEPLOYMENT-ARTIFACT-T01.** Substituted artifact fails even if name/version unchanged.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
