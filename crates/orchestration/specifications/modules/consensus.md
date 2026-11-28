# Evidence consensus

**ZIP-ORCHESTRATION-CONSENSUS-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/consensus.rs`

## Boundary and inputs

Group verified observations by candidate digest, requirement and independent principal or verifier identity. Reject out-of-scope evidence, detect divergent results from one identity and retain each dissenting receipt under its original provenance. Accept criteria come from Verification and policy. An advisory agreement has no authority to approve a write or certify release.

## Behavior and failure handling

Compare observations in stable order. Report agreement only on the matching scoped claim, disagreement when authoritative evidence conflicts, and insufficient evidence when required observations are absent or unavailable. A majority does not erase a contradiction or fill a missing required receipt. Preserve all evidence referenced by the decision, and route disagreements to the owning resolution boundary.

## Acceptance

**ZIP-ORCHESTRATION-CONSENSUS-T01.** Submit agreeing observations, one contradictory immutable receipt and a duplicate identity. Verify conflict remains blocked under any order. Remove a mandatory receipt and confirm the remaining agreement cannot satisfy the gate.
