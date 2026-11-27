# Verification crate design

**Contract version** 1.1 candidate. Master design §44. Planned implementation.

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

[Verification plan](specifications/modules/verification_plan.md) owns normalized gates and binding. [Verifier](specifications/modules/verifier.md) requests bounded observations from injected runners. [Evidence](specifications/modules/evidence.md) and [provenance](specifications/modules/provenance.md) validate actual candidate, origin and result. [Acceptance](specifications/modules/acceptance.md) evaluates qualified mandatory gates without introducing extra dependencies.

## Failure, safety and resource limits

Limit observed bytes and check duration to authorized and admitted budgets. Evidence explicitly distinguishes executed failure, missing observations and stale observations. Verify human authority and independence at manual-only gates. Reconcile ambiguous attempts before interpreting a result. Preserve historical results and scoped evidence without synthesizing success.

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

Apply the [evidence fixtures](../../contracts/acceptance/verification/evidence-fixtures.json) to candidate change, failed and missing gates, scope, reducer precedence and reviewer independence.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. The evidence and acceptance slice is a candidate for independent review. Other modules retain their recorded maturity.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`verifier.rs`](specifications/modules/verifier.md)
- [`verification_plan.rs`](specifications/modules/verification_plan.md)
- [`requirements.rs`](specifications/modules/requirements.md)
- [`acceptance.rs`](specifications/modules/acceptance.md)
- [`evidence.rs`](specifications/modules/evidence.md)
- [`provenance.rs`](specifications/modules/provenance.md)
- [`independent_review.rs`](specifications/modules/independent_review.md)
- [`reproducibility.rs`](specifications/modules/reproducibility.md)
- [`static_analysis.rs`](specifications/modules/static_analysis.md)
- [`dynamic_analysis.rs`](specifications/modules/dynamic_analysis.md)
- [`formal/mod.rs`](specifications/modules/formal/mod.md)
- [`formal/specification.rs`](specifications/modules/formal/specification.md)
- [`formal/invariants.rs`](specifications/modules/formal/invariants.md)
- [`formal/model_checking.rs`](specifications/modules/formal/model_checking.md)
- [`formal/proof_adapter.rs`](specifications/modules/formal/proof_adapter.md)
- [`repository/mod.rs`](specifications/modules/repository/mod.md)
- [`repository/diff.rs`](specifications/modules/repository/diff.md)
- [`repository/scope.rs`](specifications/modules/repository/scope.md)
- [`repository/batch.rs`](specifications/modules/repository/batch.md)
- [`repository/integration.rs`](specifications/modules/repository/integration.md)
- [`quality/mod.rs`](specifications/modules/quality/mod.md)
- [`quality/correctness.rs`](specifications/modules/quality/correctness.md)
- [`quality/completeness.rs`](specifications/modules/quality/completeness.md)
- [`quality/consistency.rs`](specifications/modules/quality/consistency.md)
- [`quality/maintainability.rs`](specifications/modules/quality/maintainability.md)
- [`reporting.rs`](specifications/modules/reporting.md)
