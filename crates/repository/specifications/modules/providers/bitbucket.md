# Bitbucket provider mapping

**ZIP-REPOSITORY-PROVIDERS-BITBUCKET-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/providers/bitbucket.rs`

## Required implementation behavior

Use stable workspace/repository identity and qualified PR capability. Keep endpoint and token audience bound; unsupported check state remains unknown.

## Acceptance

**ZIP-REPOSITORY-PROVIDERS-BITBUCKET-T01.** Unqualified checks cannot satisfy an acceptance gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
