# Approved provider routing

**ZIP-INTELLIGENCE-ROUTER-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/router.rs`

## Required implementation behavior

Filter by policy, locality, credential reference, model contract, budgets and fresh capability. Pin route and diagnostics before dispatch.

## Acceptance

**ZIP-INTELLIGENCE-ROUTER-T01.** Offline request triggers no DNS or remote inference.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
