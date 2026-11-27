# Bounded policy exception

**ZIP-GOVERNANCE-EXCEPTIONS-001 · v1.0 · Owner:** Governance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/governance/src/exceptions.rs`

## Required implementation behavior

Require specific named nonconstitutional rule, independent authority, rationale, exact scope and expiry. Apply only within allowed exception policy. Append reversible outcome and audit.

## Acceptance

**ZIP-GOVERNANCE-EXCEPTIONS-T01.** Attempt to exempt a constitutional restriction is denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
