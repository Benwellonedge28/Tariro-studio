# GitLab provider boundary

**ZIP-PROVIDERS-REPOSITORIES-GITLAB-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/repositories/gitlab.rs`

## Required implementation behavior

Pin immutable project ID and qualified branch/MR capability; translate provider-specific status without fabricating equivalence.

## Acceptance

**ZIP-PROVIDERS-REPOSITORIES-GITLAB-T01.** Renamed or reused project path cannot substitute different project identity.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
