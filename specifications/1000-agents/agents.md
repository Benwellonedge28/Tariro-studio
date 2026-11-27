# Agent lifecycle and permissions

**Contract version** 1.0. Master design §71.

## Contract

An agent manifests its role, tool capability versions, mailbox bound, model requirements and resource ceiling. Agent identity is assignment-scoped. Credential use resolves through approved adapters.

## Execution and integration

Transitions are Registered, Ready, Busy, Suspended, Draining and Stopped. Reject unsupported transitions and full mailboxes. Delegation narrows scope and expiry and records delegator lineage.

## Verification

Run two roles on the same model and verify no shared mutable context or privileges. Revocation blocks the next effect.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [agents crate design](../../crates/agents/DESIGN.md)
- [governance crate design](../../crates/governance/DESIGN.md)
