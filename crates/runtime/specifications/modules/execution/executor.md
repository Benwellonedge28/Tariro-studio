# Object-safe execution port

**ZIP-RUNTIME-EXECUTION-EXECUTOR-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for single-host execution.

**Planned source:** `crates/runtime/src/execution/executor.rs`

## Internal port

Rust-shaped pseudocode. Import `Future` and `Pin` from `std::future` and `std::pin`. `TaskSpec` comes from [task](task.md), `OwnedLaunch` and `ProcessObservation` from [supervisor](../supervisor.md), and `RuntimeError` from [errors](../error.md). Keep the trait and alias crate-private.

```rust
type AdapterFuture<'a, T> =
    Pin<Box<dyn Future<Output = Result<T, RuntimeError>> + Send + 'a>>;

trait Executor: Send + Sync {
    fn dispatch<'a>(&'a self, task: &'a TaskSpec, launch: OwnedLaunch)
        -> AdapterFuture<'a, ProcessObservation>;
}
```

Dispatch consumes the opaque, non-clonable `OwnedLaunch`. A trusted supervisor constructs it only after the verified activation and durable one-way launch claim. Polling the adapter may hand over the contained task once. Dropping its future leaves durable intent in place. Keep the underlying process obligation in the supervisor, outside the future lifetime.

## Execution and failure

1. Validate the selected adapter can establish, address and observe the attempt's containment across supervisor restart, including an interruption during preparation. Bind the installed controls and the prepared locator to the attempt. Return `ContainmentUnavailable` before execution where those guarantees are unavailable.
2. At the final gate, verify that the binding still has current job ownership, runtime generation, resource permit and effect authority where required. The composition must serialize authorization to cross this gate with observed stop/fencing for this attempt. Release the allow-execution gate exactly once. A stop after this boundary is handled as cancellation of possibly running work.
3. Return a confirmed containment-bound observation or a typed error. Only a verified refusal before any task body could run is `SpawnFailed`. An ambiguous launch, lost reply or unverifiable observation is `OutcomeUnknown`. Never use a bare PID or wall-clock timestamp to establish attempt identity.
4. The supervisor alone records the durable transition. A successful dispatch observation confirms start. Execution output and exit arrive separately. Stop, teardown and ownership inspection use the platform supervision interfaces and remain available to trusted recovery after dispatch returns.

The resource reservation covers preparation and execution. Use no unbounded adapter buffer. Expected errors and evidence follow the [supervisor](../supervisor.md) and [failure](../error.md) contracts. Native gate and platform supervision interfaces still require qualification.

## Acceptance

**ZIP-RUNTIME-EXECUTION-EXECUTOR-T01.** Two deterministic adapters must conform to the same durable observations. Cancel before opening the launch gate, then inject loss after it opens. The first case executes zero bodies. The second requires observation or recovery and has at most one start for the attempt.
