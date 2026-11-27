# Governance failure classification

**ZIP-GOVERNANCE-ERROR-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/error.rs`

## Required implementation behavior

Represent Unauthenticated, PolicyUnavailable, Denied, ApprovalRequired, StaleScope, Expired, Revoked, Conflict and Stopped. Return details only after authorized access.

## Acceptance

**ZIP-GOVERNANCE-ERROR-T01.** Unauthorized intent does not reveal policy details beyond safe reason.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
