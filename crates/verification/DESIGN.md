# Verification crate design

**Contract version** 1.0. Master design §44. Planned implementation.

## Responsibility and dependencies

Bind evidence to exact snapshot, inputs, toolchain and policy. Execute independent checks; apply fail > blocked > pass precedence. Accept only complete required evidence.

First-party dependencies: [foundation](../foundation/DESIGN.md), [repository](../repository/DESIGN.md), [storage](../storage/DESIGN.md)

- [Engineering](../../specifications/1600-engineering/engineering.md)
- [Testing](../../specifications/1900-testing/testing.md)
- [Verification](../../specifications/2100-verification/verification.md)
- [Deployment](../../specifications/3300-deployment/deployment.md)
- [Evolution](../../specifications/3500-evolution/evolution.md)
- [Acceptance](../../specifications/3600-acceptance/acceptance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `compile_plan(requirements)`
- `verify(candidate)`
- `accept(evidence_bundle)`

Record families: RequirementGate, EvidenceRecord, verifier identity, observation and verdict. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `EvidenceRecord { requirement_id, candidate_digest, policy_digest, input_digest, runner_version, actor, observed_ref, verdict }`
- `VerificationPlan { required_gates, expected_inputs }`

- `accept(plan: &VerificationPlan, evidence: &[EvidenceRecord]) -> Result<AcceptanceVerdict>`

## Failure, safety and resource limits

Evidence size and verification duration bounded. Manual-only gates require approver identity. Different agent roles do not imply independence.

- `EvidenceMissing`
- `EvidenceStale`
- `FactUnverified`
- `GateFailed`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/verification/src/
├── lib.rs
├── error.rs
├── verifier.rs
├── verification_plan.rs
├── requirements.rs
├── acceptance.rs
├── evidence.rs
├── provenance.rs
├── independent_review.rs
├── reproducibility.rs
├── static_analysis.rs
├── dynamic_analysis.rs
├── formal/
│   ├── mod.rs
│   ├── specification.rs
│   ├── invariants.rs
│   ├── model_checking.rs
│   └── proof_adapter.rs
├── repository/
│   ├── mod.rs
│   ├── diff.rs
│   ├── scope.rs
│   ├── batch.rs
│   └── integration.rs
├── quality/
│   ├── mod.rs
│   ├── correctness.rs
│   ├── completeness.rs
│   ├── consistency.rs
│   └── maintainability.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Changing candidate after review must fail. Test failed and missing mandatory evidence.
