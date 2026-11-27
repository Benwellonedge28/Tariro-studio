# Gitea provider mapping

**ZIP-REPOSITORY-PROVIDERS-GITEA-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/providers/gitea.rs`

## Required implementation behavior

Bind repository identity and configured origin, negotiate current supported ref and PR protocols. Do not reuse credentials/config from another provider.

## Acceptance

**ZIP-REPOSITORY-PROVIDERS-GITEA-T01.** Changed origin cannot inherit Gitea credential capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
