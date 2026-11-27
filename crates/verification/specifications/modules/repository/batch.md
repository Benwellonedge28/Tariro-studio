# Exact batch verification

**ZIP-VERIFICATION-REPOSITORY-BATCH-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/repository/batch.rs`

Derive distinct normalized changed outputs from the verified manifest, applying operation and both-endpoint scope before counting. Unchanged files and repeated paths cannot increase the count. Match the exact batch agreement on the grant whenever present. A larger batch fails and a short final batch stays blocked for explicit revision. The reference 30-file workflow supplies its own runtime policy. Require a qualifying independent observation for every touched path as required by the plan. Bind actual count, ordered manifest digest, evidence and gate verdict. The Assignments crate owns approvals and publication state.

**ZIP-VERIFICATION-REPOSITORY-BATCH-T01.** Duplicate paths count once. An authorized 30 with 29 distinct covered entries remains blocked.
