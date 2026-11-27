# CLI application design

**ZIP-APP-CLI-001 · v1.0 · Owner:** CLI maintainers. **Maturity:** D3. The [command reference](../../documentation/cli/commands.md) owns public syntax and exit mappings.

`main.rs` validates launch context, loads a versioned transport configuration, then dispatches one request. `arguments.rs` owns strict argument decoding and deterministic error behavior. `output.rs` formats an owned typed reply. Files under `commands/` translate arguments into gateway requests for initialization, diagnostics, repositories, assignments, agents, models, workflows, memory, security, server and mesh. No command may bypass the same policy gate used by Studio or server.

Read commands carry the workspace and selected immutable revision. Mutations also carry reviewed target and stable idempotency key or expected revision. The CLI process may detach a supervised assignment, but it never starts a background process outside runtime ownership. Local IPC is the initial transport; missing daemon or unnegotiated capability gets a typed error and documented exit status. JSON emits one result to standard output and redacted human diagnostics to standard error. A write failure cannot be rendered as a successful command.

Read a bounded amount of stdin, reject extra bytes before parsing, and route output using admitted limits. A wait deadline ends CLI observation while preserving assignment state. Ctrl-C requests cancellation only for the invocation's owned command or where explicitly authorized. Do not resolve live credentials into arguments or output.

App tests run offline with a fake gateway, compare human and JSON statuses, verify exact idempotency identity and confirm unknown outcomes remain reconcilable. Completion additionally needs per-file fixtures under the [source inventory](../../contracts/components/source-inventory.json).

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

- [`main.rs`](specifications/modules/main.md)
- [`arguments.rs`](specifications/modules/arguments.md)
- [`output.rs`](specifications/modules/output.md)
- [`commands/init.rs`](specifications/modules/commands/init.md)
- [`commands/doctor.rs`](specifications/modules/commands/doctor.md)
- [`commands/repository.rs`](specifications/modules/commands/repository.md)
- [`commands/assignment.rs`](specifications/modules/commands/assignment.md)
- [`commands/agent.rs`](specifications/modules/commands/agent.md)
- [`commands/model.rs`](specifications/modules/commands/model.md)
- [`commands/workflow.rs`](specifications/modules/commands/workflow.md)
- [`commands/memory.rs`](specifications/modules/commands/memory.md)
- [`commands/security.rs`](specifications/modules/commands/security.md)
- [`commands/server.rs`](specifications/modules/commands/server.md)
- [`commands/mesh.rs`](specifications/modules/commands/mesh.md)
