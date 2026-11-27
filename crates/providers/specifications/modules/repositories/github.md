# GitHub provider boundary

**ZIP-PROVIDERS-REPOSITORIES-GITHUB-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/repositories/github.rs`

## Required implementation behavior

Pin immutable repo ID, expected ref and reviewed operation; inspect exact result and reconcile uncertain writes without blind retry.

## Acceptance

**ZIP-PROVIDERS-REPOSITORIES-GITHUB-T01.** Lost PR creation reply resumes via matching exact marker/head.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
