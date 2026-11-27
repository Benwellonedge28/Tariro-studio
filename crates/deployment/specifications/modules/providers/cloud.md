# Explicit cloud deployment adapter

**ZIP-DEPLOYMENT-PROVIDERS-CLOUD-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/providers/cloud.rs`

## Required implementation behavior

Require exact tenant/region/service, artifact and effect permission; reconcile ambiguous scopes and spend constraints. No default cloud activation.

## Acceptance

**ZIP-DEPLOYMENT-PROVIDERS-CLOUD-T01.** Cloud permission for staging cannot authorize production promotion.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
