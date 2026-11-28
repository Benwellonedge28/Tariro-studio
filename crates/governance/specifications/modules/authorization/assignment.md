# Grant bound to an assignment

**ZIP-GOVERNANCE-AUTHORIZATION-ASSIGNMENT-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/authorization/assignment.rs`

## Boundary and inputs

Issue a grant only from an authenticated authority allowed to bind the exact assignment. Bind the recipient principal, workspace, repository identity and pinned base, approved effects and paths, locality and destination restrictions, finite applicable resource ceilings, validity, policy digest and current scope epoch. Require all attributes used by policy. Unsupported preconditions or stale base block issuance.

## Behavior and failure handling

Persist the immutable grant, active scope binding and audit/outbox intent together. Return an opaque reference, scoped to the intended principal and operation family. A repeat of the same authorized issuance command replays the receipt. Scope enlargement needs a new approved grant. Current policy may tighten enforcement without rewriting historical grant bytes. Separately privileged actions still require the [approval contract](approval.md).

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-ASSIGNMENT-T01.** Attempt issuance with missing actor, mismatched repository identity and stale pinned base. Verify no grant or accepted audit receipt. Repeat a valid issuance command and verify one stable identity. Change permitted paths under the same key and verify refusal.
