# Read-only health projection

**ZIP-OBSERVABILITY-HEALTH-001 · v1.0 · Owner:** Observability maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/observability/src/health.rs`

## Required implementation behavior

Report readiness, liveness and unavailable critical dependencies from actual observations, including age/version and redacted reasons.

## Acceptance

**ZIP-OBSERVABILITY-HEALTH-T01.** Unverified backend availability does not become ready.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
