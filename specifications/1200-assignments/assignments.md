# Persistent assignments

**Contract version** 1.0. Master design §71.

## Contract

Assignment transitions require a revision-checked command, current state, principal and evidence. Task checkpoint sequence is contiguous. Each verified unit stores path/digest, verifier version and requirement IDs before progress advances.

## Execution and integration

External intent stores effect key, expected remote state and payload digest; unknown outcome blocks retry until reconciliation. A resumed grant is checked against current policy, scope, epoch and expiry. Exact batch size is enforced before sealing.

## Verification

Replay response loss at push and PR creation. Deny unauthorized extension, 31st file, and final short batch. Resume at 18 after interruption at 17.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).

## Persisted contract and transition table

`assignments[(workspace_id, assignment_id)]` stores schema version, owner, repository ID, base commit, requirements, path and network scope, grant ID, budget, plan digest, state, revision, task IDs, artifact/evidence references, effect references and timestamps. `checkpoints[(assignment_id, unit_index)]` stores plan revision, sealed file digest, verification ID and the next step. `effects[(assignment_id, effect_key)]` stores payload digest, expected remote state, outcome, receipt and reconciler version.

| Command | From | To | Required guard |
| --- | --- | --- | --- |
| Validate | Submitted | Validated or Blocked | Strict schema, repository/instructions available |
| Authorize | Validated or AwaitingApproval | Authorized | Current matching grant |
| Plan | Authorized | Planned | Plan references immutable base and checks |
| Queue | Planned | Scheduled | Approved capacity and adapter availability |
| Start | Scheduled or Recovering | Executing | Live lease and current grant |
| Verify | Executing | Verifying | Every planned work unit has a staged result |
| Accept | Verifying | Completed | All required checks passed and external effects reconciled |
| Pause | Scheduled, Executing or Verifying | Paused | Stop admission, drain or cancel, checkpoint durable work |
| Resume | Paused or Blocked | Recovering | Revalidate grant, plan, checkpoint and outstanding effects |
| Revoke or cancel | Any nonterminal | AwaitingApproval or Cancelled | Prevent new effects, stop local processes, reconcile started effects |
| Fail | Any nonterminal executing state | Failed | Persist typed error, partial work and evidence |

Every transition compares `expected_revision` and increments it exactly once on success. A retried command with the same idempotency key and payload returns its original result. A different payload returns Conflict. Completed, Failed and Cancelled are terminal. Restart scans nonterminal records and never executes a missing or unverifiable checkpoint.

## Implementing components

- [assignments crate design](../../crates/assignments/DESIGN.md)
- [storage crate design](../../crates/storage/DESIGN.md)
- [governance crate design](../../crates/governance/DESIGN.md)
