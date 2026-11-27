# Fail-closed verdict reduction

**ZIP-VERIFICATION-ACCEPTANCE-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/acceptance.rs`

```rust
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum AcceptanceVerdict { Passed, Blocked, Failed }

pub fn accept(
    plan: &crate::verification_plan::VerificationPlan,
    evidence: &[crate::evidence::EvidenceRecord],
    candidate: &crate::verifier::CandidateSeal,
) -> Result<AcceptanceReport, crate::error::VerificationError>;
```

Resolve evidence by gate and exact selected attempt. Validate candidate, plan, policy, provenance, required independence and output bytes before considering status. An unqualified or stale failed observation remains historical and is not proof of failure on this candidate. A trusted matching mandatory failure produces Failed even if another mandatory gate is missing. Otherwise missing, stale, skipped, unavailable, cancelled, unresolved, incompatible or conflicting mandatory evidence produces Blocked. Passed requires every applicable mandatory gate passed plus no unresolved blocking findings. A verification plan without applicable gates passes only when all in-scope requirements have reviewed applicable inapplicability records and policy explicitly permits empty execution. Optional results are visible but do not promote or reduce the mandatory verdict.

Exact duplicate observations collapse. Conflicting observations for one attempt block unless a currently qualified mandatory failure already determines Failed. A later attempted pass cannot overwrite an earlier failure. Any approved supersession uses explicit attempt lineage and per-gate rerun policy; if no such policy applies, the failure stands. Keep prior results and the approval evidence on the report. Report candidate seal and plan, mandatory gate resolution, optional results, findings and scoped evidence references in stable gate order.

**ZIP-VERIFICATION-ACCEPTANCE-T01.** A current mandatory failure outranks missing evidence. An inconclusive stale failure with no current match blocks instead. Current mandatory pass evidence on all gates yields Passed.
