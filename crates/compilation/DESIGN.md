# Compilation crate design

**Contract version** 1.0. Master design §34. Planned implementation.

## Responsibility and dependencies

Resolve manifest and toolchain, build in approved sandbox with structured args, capture exit and bounded diagnostics, verify output digests before cache promotion.

First-party dependencies: [foundation](../foundation/DESIGN.md), [terminal](../terminal/DESIGN.md), [resources](../resources/DESIGN.md), [repository](../repository/DESIGN.md)

- [Compilation](../../specifications/1800-compilation/compilation.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `detect(snapshot)`
- `plan(target, profile)`
- `build(plan)`
- `artifacts(execution)`

Record families: BuildPlan, toolchain pin, build execution and artifact records. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `BuildPlan { source_revision, toolchain_digest, target, args, environment_digest, deadline }`
- `BuildObservation { status, diagnostic_ref, artifacts, toolchain_version }`

- `build(plan: BuildPlan, cancel: Cancellation) -> Result<BuildObservation>`

## Failure, safety and resource limits

Network off by default. Cache identity includes tree, toolchain, target, features and relevant environment. Never reuse a failed or partial build.

- `ToolchainMissing`
- `UnsupportedTarget`
- `BuildFailed`
- `OutputLimit`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/compilation/src/
├── lib.rs
├── error.rs
├── compiler.rs
├── toolchain.rs
├── build.rs
├── target.rs
├── environment.rs
├── diagnostics.rs
├── artifacts.rs
├── reproducibility.rs
├── cache.rs
├── dependency_resolution.rs
├── adapters/
│   ├── mod.rs
│   ├── cargo.rs
│   ├── cmake.rs
│   ├── make.rs
│   ├── gradle.rs
│   ├── maven.rs
│   ├── npm.rs
│   ├── python.rs
│   ├── go.rs
│   ├── danga.rs
│   └── generic.rs
└── verification.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Change target or compiler and verify cache miss. Failed compiler exit cannot produce success.
