# Observed bounded health gate

**ZIP-DEPLOYMENT-HEALTH-CHECK-001 · v1.0 · Owner:** Deployment maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/deployment/src/health_check.rs`

## Required implementation behavior

Probe authorized endpoints with qualified checks, declared thresholds and finite timeout. Pin target and stage identity to observations.

## Acceptance

**ZIP-DEPLOYMENT-HEALTH-CHECK-T01.** Unreachable service cannot satisfy health gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
