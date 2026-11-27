# Qualified generic repository provider

**ZIP-PROVIDERS-REPOSITORIES-GENERIC-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/repositories/generic.rs`

## Required implementation behavior

Require verified repo identity, immutable commits, scoped effects and observe/reconcile adapters for supported operations.

## Acceptance

**ZIP-PROVIDERS-REPOSITORIES-GENERIC-T01.** Unsupported remote mutation remains unavailable instead of assuming Git semantics.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
