# Checkpoint and chain validation

**ZIP-AUDIT-INTEGRITY-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/integrity.rs`

## Boundary and inputs

Read a pinned workspace snapshot and the requested range plus independently verified start and end expectations when the claim requires completeness. Verify current authorization, sequence continuity, supported format, predecessor bindings and every canonical digest. Validate configured checkpoint signatures and enrolled signer scope through Security when the policy requires them.

## Behavior and failure handling

Verify the observed tail against trusted high-water or checkpoint evidence before claiming the expected suffix is present. A chain consistent only within a returned slice cannot prove omitted records are absent. Expose verified range, unmet anchor requirements and first mismatch with redacted provenance. Never repair, overwrite or infer successful deletion from verification.

## Acceptance

**ZIP-AUDIT-INTEGRITY-T01.** Truncate a suffix beneath a separately trusted checkpoint and verify failure. Provide an internally consistent slice with no trusted tail evidence and verify full-history qualification remains blocked.
