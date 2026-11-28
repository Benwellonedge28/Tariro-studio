# Agent task delegation

**ZIP-AGENTS-DELEGATION-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/delegation.rs`

## Boundary and inputs

Accept an exact parent binding, requested task scope and bounded child role request. Verify the caller and live parent lineage through Governance. Compute child permissions from the parent, request and applicable policy, using the narrower authority and earliest deadline. Require a fresh child identity under the assignment and derive its depth by checked arithmetic.

## Behavior and failure handling

Reject cycles, stale lineage and depth beyond resolved agents.max_delegation_depth. A valid delegation defines a restricted child request. Store lineage with the approved digest through the owning boundary before submitting it. The execution owner still admits a fresh runtime attempt. Revalidate parent authority at child dispatch and effects. Revocation fences future work while preserving existing receipts and cleanup.

## Acceptance

**ZIP-AGENTS-DELEGATION-T01.** Attempt to increase role, data scope and lifetime and present a depth beyond policy. Verify no child is submitted. Revoke after accepting an in-scope child and confirm its next effect is denied.
