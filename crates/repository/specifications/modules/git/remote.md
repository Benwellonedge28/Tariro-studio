# Remote identity and configuration

**ZIP-REPOSITORY-GIT-REMOTE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/remote.rs`

## Required implementation behavior

Validate canonical approved endpoint and provider repository ID. Runtime does not inherit global remotes or arbitrary credentials. Network adapter enforces allowed destination.

## Acceptance

**ZIP-REPOSITORY-GIT-REMOTE-T01.** Remote redirect/new identity requires approval or denies.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
