# Bounded policy exception

**ZIP-GOVERNANCE-EXCEPTIONS-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/exceptions.rs`

## Boundary and inputs

Accept an exception request naming a versioned exception-eligible nonconstitutional rule, exact scope and action digest, rationale, validity and independently authenticated approving authority. Verify the rule explicitly permits this exception class. A reviewer or model cannot grant an exception merely by proposing it.

## Behavior and failure handling

Record the decision and redacted audit intent transactionally. Apply the exception only to the named rule and scope until expiry or revocation. Re-evaluate all remaining constraints normally and preserve the original decisions. Never waive a constitutional control, widen a parent grant or convert an unresolved effect to success. Changing target or scope requires a new request.

## Acceptance

**ZIP-GOVERNANCE-EXCEPTIONS-T01.** Attempt to waive a constitutional requirement and to reuse an approved exception against a different action. Both deny. Expire a valid exception and verify future evaluations apply the original restriction.
