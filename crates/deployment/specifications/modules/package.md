# Bounded package validation

**ZIP-DEPLOYMENT-PACKAGE-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/package.rs`

## Required implementation behavior

Check canonical manifest, expected entries, path confinement and admitted size before extracting to owned staging. No unsigned fallback where required.

## Acceptance

**ZIP-DEPLOYMENT-PACKAGE-T01.** Traversal path or duplicate entry rejected before activation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
