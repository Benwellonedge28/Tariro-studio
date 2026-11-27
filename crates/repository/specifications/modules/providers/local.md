# Offline local repository provider

**ZIP-REPOSITORY-PROVIDERS-LOCAL-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/providers/local.rs`

## Required implementation behavior

Use owned rooted worktree with immutable commit identity and structured Git operations. Remote PR/check capability is explicitly unavailable. No externally fetched info during local operation.

## Acceptance

**ZIP-REPOSITORY-PROVIDERS-LOCAL-T01.** Offline deterministic fixture exercises inspect, staged diff and approved commit without DNS.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
