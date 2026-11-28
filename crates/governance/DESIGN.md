# Governance crate design

**Contract version** 1.1 candidate. Master design §43. Planned implementation.

## Responsibility and dependencies

Intersect the constitution, active policy and exact scoped grant. Evaluate a redacted decision before the authorized claim records durable intent. Record revocation and stop before notifying execution owners. Runtime and Resources own process containment, lease holds and verified release.

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

Record families: Authorization, PolicyVersion, Decision, ApprovalRequest and revocation epoch. [Evaluation](specifications/modules/policy_engine.md) produces observations and [claim](specifications/modules/authorization/operation.md) records a guarded intent. Composition supplies the required Audit participant through the shared Storage transaction, with no new first-party dependency. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

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

## Planned source-file contracts

Every planned Governance source path has a candidate file contract. See the [requirements map](../../contracts/requirements/modules/governance.json). Exact Rust port signatures, active clock and authority qualification, and independent design review remain open.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`constitution.rs`](specifications/modules/constitution.md)
- [`policy.rs`](specifications/modules/policy.md)
- [`policy_engine.rs`](specifications/modules/policy_engine.md)
- [`decision.rs`](specifications/modules/decision.md)
- [`rules.rs`](specifications/modules/rules.md)
- [`constraints.rs`](specifications/modules/constraints.md)
- [`authorization/mod.rs`](specifications/modules/authorization/mod.md)
- [`authorization/assignment.rs`](specifications/modules/authorization/assignment.md)
- [`authorization/operation.rs`](specifications/modules/authorization/operation.md)
- [`authorization/approval.rs`](specifications/modules/authorization/approval.md)
- [`authorization/delegation.rs`](specifications/modules/authorization/delegation.md)
- [`authorization/expiry.rs`](specifications/modules/authorization/expiry.md)
- [`authorization/revocation.rs`](specifications/modules/authorization/revocation.md)
- [`oversight/mod.rs`](specifications/modules/oversight/mod.md)
- [`oversight/human.rs`](specifications/modules/oversight/human.md)
- [`oversight/escalation.rs`](specifications/modules/oversight/escalation.md)
- [`oversight/intervention.rs`](specifications/modules/oversight/intervention.md)
- [`oversight/emergency_stop.rs`](specifications/modules/oversight/emergency_stop.md)
- [`compliance.rs`](specifications/modules/compliance.md)
- [`exceptions.rs`](specifications/modules/exceptions.md)
- [`evaluation.rs`](specifications/modules/evaluation.md)
