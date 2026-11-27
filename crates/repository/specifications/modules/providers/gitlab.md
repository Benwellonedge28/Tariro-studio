# GitLab provider mapping

**ZIP-REPOSITORY-PROVIDERS-GITLAB-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/providers/gitlab.rs`

## Required implementation behavior

Resolve immutable project ID; map merge-request labels and state to common receipt while preserving provider IDs. Unadvertised capability denies. Separate branch push authorization.

## Acceptance

**ZIP-REPOSITORY-PROVIDERS-GITLAB-T01.** Same project path reused with different project ID blocks effect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
