# Governance crate design

**Contract version** 1.0. Master design §43. Planned implementation.

## Responsibility and dependencies

Intersect signed/owner policies and agent capabilities, hash exact scope and inputs, re-evaluate immediately before effect, persist intent and invalidate scoped leases on revoke.

First-party dependencies: [foundation](../foundation/DESIGN.md), [identity](../identity/DESIGN.md), [security](../security/DESIGN.md), [storage](../storage/DESIGN.md), [events](../events/DESIGN.md)

- [Agents](../../specifications/1000-agents/agents.md)
- [Assignments](../../specifications/1200-assignments/assignments.md)
- [Governance](../../specifications/2400-governance/governance.md)
- [Evolution](../../specifications/3500-evolution/evolution.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `evaluate(operation)`
- `grant(scope)`
- `authorize_once(action)`
- `revoke(grant)`
- `stop(scope)`

Record families: Authorization, PolicyVersion, Decision, ApprovalRequest and revocation epoch. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Grant { principal, repository, revision, effects, paths, destinations, budgets, policy_digest, expiry, epoch }`
- `ApprovalRequest { id, effect_digest, required_role, expires_at }`

- `evaluate(operation: EffectRequest, grant: GrantRef) -> Result<GovernanceDecision>`

## Failure, safety and resource limits

Human approval required for separately privileged operations regardless of agent vote. Stop is durable and blocks new effects; grant never auto-expands.

- `PolicyDenied`
- `AwaitingApproval`
- `Expired`
- `Revoked`
- `EmergencyStopped`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/governance/src/
├── lib.rs
├── error.rs
├── constitution.rs
├── policy.rs
├── policy_engine.rs
├── decision.rs
├── rules.rs
├── constraints.rs
├── authorization/
│   ├── mod.rs
│   ├── assignment.rs
│   ├── operation.rs
│   ├── approval.rs
│   ├── delegation.rs
│   ├── expiry.rs
│   └── revocation.rs
├── oversight/
│   ├── mod.rs
│   ├── human.rs
│   ├── escalation.rs
│   ├── intervention.rs
│   └── emergency_stop.rs
├── compliance.rs
├── exceptions.rs
└── evaluation.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test missing attributes, grant expiry during execution, and policy change before external write.
