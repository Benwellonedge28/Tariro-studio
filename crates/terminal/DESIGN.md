# Terminal crate design

**Contract version** 1.1 candidate. Master design §39. Planned implementation.

## Responsibility and dependencies

Resolve allowed executable, spawn directly with structured arguments and scrub environment, spool bounded output, enforce timeout and reap children.

First-party dependencies: [foundation](../foundation/DESIGN.md), [sandbox](../sandbox/DESIGN.md), [resources](../resources/DESIGN.md)

- [Compilation](../../specifications/1800-compilation/compilation.md)
- [Tools](../../specifications/2200-tools/tools.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `start(CommandSpec)`
- `stream(handle)`
- `stop(handle)`

Record families: CommandSpec with executable identity, argv, cwd, env allowlist, limits and receipt. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `CommandSpec { executable_ref, argv, workspace_root_ref, cwd, environment_refs, timeout_ms, output_limit_bytes }`
- `ProcessReceipt { status, stdout_ref, stderr_ref, cleanup }`

- `start(spec: CommandSpec, sandbox: SandboxLease, cancel: Cancellation) -> Result<ProcessHandle>`

The [execution boundary](specifications/modules/execution.md) prepares through Sandbox and the trusted supervisor controls launch. [Output limits](specifications/modules/output_limits.md) apply one combined budget to both streams. Process exit, effect settlement and verified tree cleanup remain independent observations.

## Failure, safety and resource limits

No shell by default. Interactive shell requires user intent and sandbox. Bound combined standard streams and execution with `terminal.max_output_bytes` and `terminal.deadline_ms` under the admitted task lease.

- `ExecutableDenied`
- `SpawnFailed`
- `Timeout`
- `OutputLimit`
- `CleanupIncomplete`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/terminal/src/
├── lib.rs
├── error.rs
├── command.rs
├── arguments.rs
├── environment.rs
├── process.rs
├── execution.rs
├── stdin.rs
├── stdout.rs
├── stderr.rs
├── output_limits.rs
├── timeout.rs
├── cancellation.rs
├── process_tree.rs
├── working_directory.rs
├── allowlist.rs
├── policy.rs
└── audit.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test shell metacharacters as literal argv, child processes and output flooding.

## Planned source-file contracts

Every planned source path has a candidate contract and stable acceptance mapping in the [requirements map](../../contracts/requirements/modules/terminal.json). Compiled native argv and working-directory proofs, native process-tree qualification and independent review remain open.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`command.rs`](specifications/modules/command.md)
- [`arguments.rs`](specifications/modules/arguments.md)
- [`environment.rs`](specifications/modules/environment.md)
- [`process.rs`](specifications/modules/process.md)
- [`execution.rs`](specifications/modules/execution.md)
- [`stdin.rs`](specifications/modules/stdin.md)
- [`stdout.rs`](specifications/modules/stdout.md)
- [`stderr.rs`](specifications/modules/stderr.md)
- [`output_limits.rs`](specifications/modules/output_limits.md)
- [`timeout.rs`](specifications/modules/timeout.md)
- [`cancellation.rs`](specifications/modules/cancellation.md)
- [`process_tree.rs`](specifications/modules/process_tree.md)
- [`working_directory.rs`](specifications/modules/working_directory.md)
- [`allowlist.rs`](specifications/modules/allowlist.md)
- [`policy.rs`](specifications/modules/policy.md)
- [`audit.rs`](specifications/modules/audit.md)
