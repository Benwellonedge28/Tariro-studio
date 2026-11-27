# Last-moment effect check

**ZIP-GOVERNANCE-AUTHORIZATION-OPERATION-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/authorization/operation.rs`

## Required implementation behavior

Recheck current revocation epoch, approved digest, resource lease, exact path and authenticated actor immediately before claiming effect; atomically persist intent with effective decision.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-OPERATION-T01.** Revoke after preview before claim denies new external dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
