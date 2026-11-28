# Independent reviewer routing

**ZIP-ORCHESTRATION-STRATEGIES-INDEPENDENT-REVIEW-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/independent_review.rs`

## Boundary and inputs

Bind an independent review request to the exact candidate digest, required checks, author principal and governed reviewer eligibility. Check qualified actor lineage, conflicts of interest declared by policy and candidate scope. Distinct role names do not establish distinct principals. Treat a different agent session operated by the same disallowed principal as ineligible.

## Behavior and failure handling

Resolve requirements through Verification and compare each review result with its assigned candidate, scope and reviewer provenance. A candidate change invalidates acceptance evidence for the older digest. If independence is required and no reviewer qualifies, return a blocked decision. Shared model infrastructure alone supplies neither eligibility nor proof of independence.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-INDEPENDENT-REVIEW-T01.** Offer one principal in two roles and a separately qualified reviewer. Reject the first and bind the second to the pinned candidate. Replace candidate bytes and verify the earlier review cannot satisfy the new acceptance gate.
