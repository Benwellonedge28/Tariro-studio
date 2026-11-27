# Runtime and scheduling

**Contract version** 1.0. Master design §71.

## Contract

TaskState is Queued, Leased, Running, Cancelling, Succeeded, Failed, Cancelled or RecoveryRequired. Write Leased plus attempt epoch before spawn. The epoch must match to accept a worker result. Keep process-tree ownership and resource lease through cleanup, even after the request ends.

## Execution and integration

Use exclusive outbox cursors, foreground Ctrl-C requests cancellation, and daemon exit drains according to the configured deadline. Only the current fenced lease may checkpoint. After restart, inspect prior task ownership and intent before claiming another attempt.

## Verification

Kill before spawn, after spawn and after durable result. Replay an event twice and verify the task result is accepted once.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [runtime crate design](../../crates/runtime/DESIGN.md)
- [scheduler crate design](../../crates/scheduler/DESIGN.md)
- [events crate design](../../crates/events/DESIGN.md)
