# Authorized manual control

**ZIP-GOVERNANCE-OVERSIGHT-INTERVENTION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/oversight/intervention.rs`

## Boundary and inputs

Accept a scoped authenticated request to pause, deny, resume or narrow an assignment. Bind exact target, old revision, proposed transition and operator authority. Verify current policy and affected evidence before delegating the transition to its owning journal. Resume cannot widen scope or skip unresolved cleanup.

## Behavior and failure handling

Use the expected revision CAS and keep a redacted immutable record of the operator decision. A conflicting concurrent command must reread and obtain fresh authority where needed. Exact replays return the prior receipt. Record ambiguous transitions under their original identity. Request process control only through the normal supervising owner.

## Acceptance

**ZIP-GOVERNANCE-OVERSIGHT-INTERVENTION-T01.** Race pause and resume on the same valid old revision and confirm one accepted change. Submit an otherwise valid resume while one effect is unresolved and verify it cannot open execution.
