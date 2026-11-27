# Memory authority isolation

**ZIP-MEMORY-SCOPE-001 · v1.0 · Owner:** Memory maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/memory/src/scope.rs`

## Required implementation behavior

Match actor, workspace, assignment/repository and approved operation before access and sharing. Scope narrowing never broadens audience.

## Acceptance

**ZIP-MEMORY-SCOPE-T01.** Cross-tenant lookup denies before ranking.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
