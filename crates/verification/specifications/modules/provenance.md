# Evidence origin integrity

**ZIP-VERIFICATION-PROVENANCE-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/provenance.rs`

Resolve visible evidence through the pinned adapter. Verify issuer/assessor identity, authorized scope, exact candidate, expected gate/input digest and immutable output bytes in that order. For source citations resolve repository ID, pinned commit, canonical path, blob identity and cited range. Compare the bounded range with the asserted observation. For CI, require completed observations for the registered check identity and exact expected commit; an approximate name match or an earlier PR head is insufficient. Reject truncated results or unverifiable signatures when required. Keep mismatched data available only as appropriately scoped failure evidence.

An agent's explanation can accompany a record but cannot supply issuer authority, test execution or evidence bytes. Distinguish observed, derived and unverified claims. Hashing an untrusted claim proves its stability, not its factual origin. Reopen evidence when a dependency, rule, trust identity or policy changes in a way the registered gate cannot validate.

**ZIP-VERIFICATION-PROVENANCE-T01.** A fabricated citation and a completed CI check for the wrong commit are rejected without being counted as current failures or passes.
