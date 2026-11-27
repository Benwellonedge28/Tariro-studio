# GitHub provider mapping

**ZIP-REPOSITORY-PROVIDERS-GITHUB-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/providers/github.rs`

## Required implementation behavior

Bind authenticated repository immutable ID; use typed API/client refs, conditional branch semantics where available, and exact PR/base/head/marker reconciliation. Scope token to adapter only.

## Acceptance

**ZIP-REPOSITORY-PROVIDERS-GITHUB-T01.** Lost push or PR acknowledgement reconciles one expected checked result.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
