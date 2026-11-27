# Agents crate design

**Contract version** 1.0. Master design §26. Planned implementation.

## Responsibility and dependencies

Instantiate declared role, attenuate delegated capabilities, admit using runtime, route proposals through verification, and drain mailbox on stop. Pin agent memory to assignment scope.

First-party dependencies: [foundation](../foundation/DESIGN.md), [governance](../governance/DESIGN.md), [intelligence](../intelligence/DESIGN.md), [runtime](../runtime/DESIGN.md)

- [Agents](../../specifications/1000-agents/agents.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `register(manifest)`
- `dispatch(agent, task)`
- `suspend(id)`
- `stop(id)`

Record families: AgentManifest, scoped principal, mailbox and lifecycle record. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `AgentManifest { role, capability_versions, model_requirements, limits }`
- `AgentState { id, principal_id, assignment_id, lifecycle, mailbox_cursor }`

- `dispatch(agent: AgentId, task: AgentTask, grant: GrantRef) -> Result<AgentTaskReceipt>`

## Failure, safety and resource limits

Bound mailbox to 128 and delegation depth to 4. Stop dispatch on revoke or exhaustion. Model identity never conveys a role.

- `CapabilityDenied`
- `MailboxFull`
- `AgentStopped`
- `DelegationLimit`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/agents/src/
├── lib.rs
├── error.rs
├── agent.rs
├── identity.rs
├── manifest.rs
├── capabilities.rs
├── lifecycle.rs
├── state.rs
├── context.rs
├── execution.rs
├── communication.rs
├── mailbox.rs
├── registry.rs
├── factory.rs
├── supervision.rs
├── delegation.rs
├── collaboration.rs
├── evaluation.rs
├── permissions.rs
├── limits.rs
├── roles/
│   ├── mod.rs
│   ├── coordinator.rs
│   ├── researcher.rs
│   ├── architect.rs
│   ├── planner.rs
│   ├── documentation.rs
│   ├── developer.rs
│   ├── reviewer.rs
│   ├── tester.rs
│   ├── debugger.rs
│   ├── security.rs
│   ├── database.rs
│   ├── performance.rs
│   ├── devops.rs
│   ├── release.rs
│   ├── compliance.rs
│   ├── maintenance.rs
│   ├── repository.rs
│   └── auditor.rs
└── metrics.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test shared model isolated context and agent blocked from self-elevation.
