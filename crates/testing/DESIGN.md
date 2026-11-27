# Testing crate design

**Contract version** 1.0. Master design §35. Planned implementation.

## Responsibility and dependencies

Select test adapter, run pinned tests with explicit seed/environment, classify every result, normalize report and preserve raw evidence. Require designated suites.

First-party dependencies: [foundation](../foundation/DESIGN.md), [terminal](../terminal/DESIGN.md), [compilation](../compilation/DESIGN.md), [verification](../verification/DESIGN.md)

- [Testing](../../specifications/1900-testing/testing.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `discover(snapshot)`
- `run(plan)`
- `parse(report)`
- `compare_baseline(results)`

Record families: TestCaseId, TestPlan, TestResult, flake history and raw report artifact. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `TestPlan { candidate, suite_ids, seed, environment_digest, isolation }`
- `TestOutcome { case_id, attempt, status, elapsed_ms, report_ref }`

- `run(plan: TestPlan, cancel: Cancellation) -> Result<TestObservations>`

## Failure, safety and resource limits

No success for missing/empty expected reports. Retry flakes only under policy, preserving failed attempts. Coverage is separate from correctness.

- `RunnerMissing`
- `ReportInvalid`
- `TestFailed`
- `CoverageUnavailable`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/testing/src/
├── lib.rs
├── error.rs
├── discovery.rs
├── test_case.rs
├── test_suite.rs
├── generation.rs
├── execution.rs
├── fixtures.rs
├── isolation.rs
├── assertions.rs
├── coverage.rs
├── results.rs
├── regression.rs
├── property_based.rs
├── mutation.rs
├── fuzzing.rs
├── integration.rs
├── end_to_end.rs
├── performance.rs
├── security.rs
├── flaky_detection.rs
└── reporting.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test malformed reports, skipped and timeout distinctions, and flake history.
