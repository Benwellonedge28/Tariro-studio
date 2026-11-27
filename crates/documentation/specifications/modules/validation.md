# Document verification gates

**ZIP-DOCUMENTATION-VALIDATION-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/validation.rs`

Check admitted Markdown decoding, role-specific required sections, links and anchors, claim evidence, tested or planned claims, dependency consistency and traceability. Tie each result to candidate bytes, plan digest, policy, verifier and source snapshot. Treat raw HTML, command snippets and links as data. A template can establish structure only. A conforming structure with an unsupported factual claim cannot pass. Require scope-qualified independent review where the plan specifies it. A placeholder finding stays unresolved until corrected or disproven; examples of placeholder text are reviewed in context.

Resolve local links against the approved candidate overlay of the pinned tree. Use the versioned renderer's heading/anchor rules and reject escaping paths. A forward cross-link to a later approved unit may be checked in the per-file gate against the target path and anchor frozen in the approved plan. Record that as an explicit final-tree obligation rather than claiming that the target already exists. All retained links and obligations must resolve byte-for-byte at final batch verification, before publication. An unplanned missing target is an immediate blocker.

Apply [verification evidence](../../../verification/specifications/modules/evidence.md) to settle every mandatory gate. A comparably checked per-file candidate can checkpoint, but final-tree obligations are mandatory at sealing. Return no success on partial reads, loss of evidence, unavailable reviewers or unmeasured readiness.

**ZIP-DOCUMENTATION-VALIDATION-T01.** Reject a well-formed document with a false claim. A planned forward anchor can pass its local obligation check; a final tree lacking that anchor cannot seal.
