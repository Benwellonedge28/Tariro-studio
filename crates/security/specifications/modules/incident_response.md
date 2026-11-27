# Scoped incident lifecycle

**ZIP-SECURITY-INCIDENT-RESPONSE-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/incident_response.rs`

## Required implementation behavior

Durably pause affected effects, revoke scope, preserve redacted evidence, reconcile pending outcomes and require reviewed recovery. Keep evidence retention authority independent.

## Acceptance

**ZIP-SECURITY-INCIDENT-RESPONSE-T01.** Restart resumes incident state and does not reenable paused capability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
