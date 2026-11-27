# Bounded rollout strategy selection

**ZIP-DEPLOYMENT-STRATEGY-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/strategy.rs`

## Required implementation behavior

Select approved steps and health gates per target, resource and blast-radius policy. Unsupported strategy blocks rather than silently expanding reach.

## Acceptance

**ZIP-DEPLOYMENT-STRATEGY-T01.** A staged rollout cannot become all-at-once by fallback.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
