# Grant bound to an assignment

**ZIP-GOVERNANCE-AUTHORIZATION-ASSIGNMENT-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/authorization/assignment.rs`

## Required implementation behavior

Issue grant only from authenticated authorized owner with workspace and repository IDs, pinned base, effect/path scopes, deadline, budgets and policy digest. Persist immutable grant and active epoch.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-ASSIGNMENT-T01.** Missing actor or stale pinned revision prevents grant creation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
