# Grant expiry and clock checks

**ZIP-GOVERNANCE-AUTHORIZATION-EXPIRY-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/authorization/expiry.rs`

## Required implementation behavior

Compare trusted current time with expiry using strict half-open validity. Clock uncertainty at authorization boundary denies. Monotonic deadlines apply only within process execution.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-EXPIRY-T01.** At exact expiry disallow new effects; clock rollback cannot revive revoked grant.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
