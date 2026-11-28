# Agent outcome qualification

**ZIP-AGENTS-EVALUATION-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/evaluation.rs`

## Boundary and inputs

Accept the pinned candidate and ordered mandatory requirement bindings, observed evidence and reviewer eligibility. Present model quality, uncertainty and observed acceptance as separate fields. Verify evidence through the owning [verification contract](../../../../specifications/2100-verification/verification.md) before computing a completion verdict.

## Behavior and failure handling

Missing, skipped, conflicting or stale evidence blocks the corresponding required criterion. Agreement, model confidence and aggregate performance cannot satisfy it. Keep passing and failing observations bound to their original candidate digests. Output a bounded verdict with requirement IDs and evidence references, with no authorization effect.

## Acceptance

**ZIP-AGENTS-EVALUATION-T01.** Use a high score with one mandatory skipped assertion, and pass evidence from another candidate. Both stay blocked. Replace with current independent evidence and verify it satisfies only the assessed criterion.
