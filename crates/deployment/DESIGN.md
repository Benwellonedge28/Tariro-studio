# Deployment crate design

**Contract version** 1.0. Master design §55. Planned implementation.

## Responsibility and dependencies

Verify release digest, provenance and gate evidence, stage to selected target, require production grant, check health, and stop or roll back per approved plan.

First-party dependencies: [foundation](../foundation/DESIGN.md), [verification](../verification/DESIGN.md), [governance](../governance/DESIGN.md), [storage](../storage/DESIGN.md), [networking](../networking/DESIGN.md)

- [Deployment](../../specifications/3300-deployment/deployment.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `stage(bundle)`
- `approve(target)`
- `release(plan)`
- `rollback(version)`

Record families: ReleaseManifest, signed artifacts, deployment intent and rollout receipt. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ReleaseManifest { artifact_refs, target, toolchain, sbom_ref, evidence_refs, signature }`
- `DeploymentIntent { target, prior_version, release_digest, approved_grant }`

- `release(plan: DeploymentIntent, cancel: Cancellation) -> Result<EffectOutcome<DeploymentReceipt>>`

## Failure, safety and resource limits

No automatic production release from compilation. Reconcile ambiguous remote stage. Roll back only to compatible verified state.

- `SignatureInvalid`
- `ReleaseDenied`
- `HealthCheckFailed`
- `RollbackBlocked`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/deployment/src/
├── lib.rs
├── error.rs
├── environment.rs
├── artifact.rs
├── package.rs
├── release.rs
├── signing.rs
├── verification.rs
├── strategy.rs
├── approval.rs
├── rollout.rs
├── rollback.rs
├── health_check.rs
├── providers/
│   ├── mod.rs
│   ├── local.rs
│   ├── container.rs
│   ├── server.rs
│   └── cloud.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test package substitution, partial rollout and failed health verification.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`environment.rs`](specifications/modules/environment.md)
- [`artifact.rs`](specifications/modules/artifact.md)
- [`package.rs`](specifications/modules/package.md)
- [`release.rs`](specifications/modules/release.md)
- [`signing.rs`](specifications/modules/signing.md)
- [`verification.rs`](specifications/modules/verification.md)
- [`strategy.rs`](specifications/modules/strategy.md)
- [`approval.rs`](specifications/modules/approval.md)
- [`rollout.rs`](specifications/modules/rollout.md)
- [`rollback.rs`](specifications/modules/rollback.md)
- [`health_check.rs`](specifications/modules/health_check.md)
- [`providers/mod.rs`](specifications/modules/providers/mod.md)
- [`providers/local.rs`](specifications/modules/providers/local.md)
- [`providers/container.rs`](specifications/modules/providers/container.md)
- [`providers/server.rs`](specifications/modules/providers/server.md)
- [`providers/cloud.rs`](specifications/modules/providers/cloud.md)
- [`reporting.rs`](specifications/modules/reporting.md)
