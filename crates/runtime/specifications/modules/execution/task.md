# Immutable task execution specification

**ZIP-RUNTIME-EXECUTION-TASK-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate.

**Planned source:** `crates/runtime/src/execution/task.rs`

## API and data

Rust-shaped pseudocode. Import `Identifier` from `foundation::identity::identifier` and `Digest` from `foundation::types::digest`. Use `std::num::NonZeroU64` for the attempt number and `std::time::Instant` for the live deadline.

```rust
pub struct TaskSpec {
    task: Identifier,
    assignment: Identifier,
    attempt_number: NonZeroU64,
    reviewed_plan: Digest,
    action: Digest,
    deadline: Instant,
}
```

Expose read-only accessors and a crate-private constructor returning `Result<TaskSpec, RuntimeError>` from those six inputs. Validate Task and Assignment kinds and store validated fields immutably. The action digest identifies the exact versioned, typed action in the reviewed plan, including capability binding and normalized parameters. The composer supplies the verified artifact reference. The worker receives neither a credential nor a mutable copy of authorization.

## Validation and integration

Before admission or any launch claim, verify that the approved plan contains this action for the assignment and task. Bind the same attempt number to the scheduler claim and the resource reservation through the trusted composer. During replay compare task, assignment, attempt and digests against the durable intent. Reject different data for a prior attempt. Revalidate the live grant and deadline on the actual execution boundary under [supervision](../supervisor.md). A validated `TaskSpec` carries execution data only. Until a Leased record commits, the submitting composer retains the reservation cleanup obligation. If registration is ambiguous, reconcile the attempt record before either side acts on that obligation.

Persist the typed IDs, attempt number and both digests using the supervisor's versioned record. The in-memory deadline cannot be serialized into usable authority. Replanning or deadline extension requires a separately authorized new attempt. Validation itself has no independent persistence mutation, adapter call or resource acquisition.

## Acceptance

**ZIP-RUNTIME-EXECUTION-TASK-T01.** Substitute the reviewed action or claim binding and verify rejection before a launch claim or adapter call. The matching case must bind the same attempt in both journals. See the [lifecycle fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).
