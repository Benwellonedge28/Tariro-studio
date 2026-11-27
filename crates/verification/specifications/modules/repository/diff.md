# Exact change evidence

**ZIP-VERIFICATION-REPOSITORY-DIFF-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/repository/diff.rs`

Use the [repository diff contract](../../../../repository/specifications/modules/git/diff.md) to compare the pinned base and reviewed tree. Verify provider repository identity, object format, old/new paths, operations, modes and old/new blob IDs by immutable snapshot. Reject incomplete scans, truncation and mismatched manifest digests. Do not open outside-worktree references or apply lenient path normalization. Store verified change evidence and exact covered path set. A changed candidate recomputes the seal and invalidates prior passing evidence.

**ZIP-VERIFICATION-REPOSITORY-DIFF-T01.** A truncated scan cannot certify changed paths, even when every visible file is authorized.
