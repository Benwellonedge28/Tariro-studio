# Agents crate design

**Contract version** 1.1 candidate. Master design §26. Planned implementation.

## Responsibility and dependencies

Instantiate the pinned role, attenuate delegated capabilities, admit through Runtime, and route proposals through verification. Close intake on stop and retain unsettled work until verified cleanup. Keep identity, private context and mutable state assignment-scoped, including when roles share a model.

First-party dependencies: [foundation](../foundation/DESIGN.md), [governance](../governance/DESIGN.md), [intelligence](../intelligence/DESIGN.md), [runtime](../runtime/DESIGN.md)

- [Agents](../../specifications/1000-agents/agents.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `register(manifest)`
- `dispatch(agent, task)`
- `suspend(id)`
- `stop(id)`

Record families: AgentManifest, scoped principal, mailbox and lifecycle record. [Role descriptors](specifications/modules/roles/mod.md) define proposal and evidence families. [Communication](specifications/modules/communication.md) and [evaluation](specifications/modules/evaluation.md) preserve the distinction between untrusted proposals and verified outcomes. Live authority is checked at the [effect boundary](specifications/modules/permissions.md). Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `AgentManifest { role, capability_versions, model_requirements, limits }`
- `AgentState { id, principal_id, assignment_id, lifecycle, mailbox_cursor }`

- `dispatch(agent: AgentId, task: AgentTask, grant: GrantRef) -> Result<AgentTaskReceipt>`

## Failure, safety and resource limits

Use `agents.max_mailbox_items` and `agents.max_delegation_depth`, tightened by scope and admitted memory. Stop dispatch on revoke or exhaustion. Model identity never conveys a role.

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

## Planned source-file contracts

Every planned Agents source path now has a candidate file contract. The [requirements map](../../contracts/requirements/modules/agents.json) binds source paths and stable acceptance identifiers. Compiled signatures, qualified adapters and independent design review remain open.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`agent.rs`](specifications/modules/agent.md)
- [`identity.rs`](specifications/modules/identity.md)
- [`manifest.rs`](specifications/modules/manifest.md)
- [`capabilities.rs`](specifications/modules/capabilities.md)
- [`lifecycle.rs`](specifications/modules/lifecycle.md)
- [`state.rs`](specifications/modules/state.md)
- [`context.rs`](specifications/modules/context.md)
- [`execution.rs`](specifications/modules/execution.md)
- [`communication.rs`](specifications/modules/communication.md)
- [`mailbox.rs`](specifications/modules/mailbox.md)
- [`registry.rs`](specifications/modules/registry.md)
- [`factory.rs`](specifications/modules/factory.md)
- [`supervision.rs`](specifications/modules/supervision.md)
- [`delegation.rs`](specifications/modules/delegation.md)
- [`collaboration.rs`](specifications/modules/collaboration.md)
- [`evaluation.rs`](specifications/modules/evaluation.md)
- [`permissions.rs`](specifications/modules/permissions.md)
- [`limits.rs`](specifications/modules/limits.md)
- [`roles/mod.rs`](specifications/modules/roles/mod.md)
- [`roles/coordinator.rs`](specifications/modules/roles/coordinator.md)
- [`roles/researcher.rs`](specifications/modules/roles/researcher.md)
- [`roles/architect.rs`](specifications/modules/roles/architect.md)
- [`roles/planner.rs`](specifications/modules/roles/planner.md)
- [`roles/documentation.rs`](specifications/modules/roles/documentation.md)
- [`roles/developer.rs`](specifications/modules/roles/developer.md)
- [`roles/reviewer.rs`](specifications/modules/roles/reviewer.md)
- [`roles/tester.rs`](specifications/modules/roles/tester.md)
- [`roles/debugger.rs`](specifications/modules/roles/debugger.md)
- [`roles/security.rs`](specifications/modules/roles/security.md)
- [`roles/database.rs`](specifications/modules/roles/database.md)
- [`roles/performance.rs`](specifications/modules/roles/performance.md)
- [`roles/devops.rs`](specifications/modules/roles/devops.md)
- [`roles/release.rs`](specifications/modules/roles/release.md)
- [`roles/compliance.rs`](specifications/modules/roles/compliance.md)
- [`roles/maintenance.rs`](specifications/modules/roles/maintenance.md)
- [`roles/repository.rs`](specifications/modules/roles/repository.md)
- [`roles/auditor.rs`](specifications/modules/roles/auditor.md)
- [`metrics.rs`](specifications/modules/metrics.md)
