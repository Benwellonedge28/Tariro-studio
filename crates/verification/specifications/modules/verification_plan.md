# Deterministic verification plan

**ZIP-VERIFICATION-VERIFICATION-PLAN-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/verification_plan.rs`

Freeze the immutable candidate identity, requirements revision, effective policy digest, authority reference, registered gate descriptors and admitted limits before issuing checks. A gate includes stable gate ID, requirement IDs, mandatory flag, exact evidence source, applicability rule, execution or manual approval mode, expected observed outputs, input and fixture digests, runner identity and supported version, independence constraint and resource limits. A post-publication gate also binds the immutable provider repository identity and expected commit. Validate complete references, reject duplicate gate IDs, deny unresolved mandatory applicability and require a known runner or reviewer contract.

Sort gate IDs and all named inputs by exact UTF-8 bytes. Use versioned type tags, fixed-width big-endian numeric fields and length prefixes for canonical variable-width fields. Sort set-valued fields, preserve deliberately ordered commands and fixtures. Digest exact candidate, policy and requirements snapshots with the normalized plan. Reordering equivalent gate declarations does not change the semantic digest. Changed gate meaning, mandatory status, policy or target requires a new plan. Qualify the codec through golden vectors before independent approval.

**ZIP-VERIFICATION-VERIFICATION-PLAN-T01.** Reject duplicate gate IDs and unknown mandatory runner contracts before dispatch. Verify permuted set fields produce stable ordering.
