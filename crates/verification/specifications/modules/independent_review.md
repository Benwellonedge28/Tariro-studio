# Independent reviewer gate

**ZIP-VERIFICATION-INDEPENDENT-REVIEW-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/independent_review.rs`

A manual-only gate requires an authenticated human reviewer from the approved reviewer domain. Compare principal identity and registered conflicts against candidate authors, contributing agents and approval policy before accepting review. Record reviewer, candidate and plan digest, review evidence, applicable findings and disposition. Different role names, sessions or instances of the same model do not establish independence. A claim of independent execution qualifies only under the declared gate policy and verified runner provenance.

Require each blocking finding to be resolved with scoped immutable evidence and a verified decision. An approval cannot erase an observed failure. Reject stale review when the candidate or applicable constraints change. Evidence from the original review remains historical. Treat unknown affiliation or unavailable reviewer evidence as Blocked.

**ZIP-VERIFICATION-INDEPENDENT-REVIEW-T01.** Deny self-review under an independent gate and repeated model output masquerading as independent manual review.
