# Persistent assignments

**Contract version** 1.1 candidate. Master design §§28 and 71.

Assignments owns an authorized plan, state revision, worker epoch, verified prefix and publication intents. Runtime owns live execution and teardown. Storage commits assignment changes, receipts and Events outbox entries atomically. Composition injects scheduler, runtime and repository adapters without changing crate dependency direction.

## Normative lifecycle

Use a revision-checked [transition command](../../crates/assignments/specifications/modules/transitions.md). Only the following command and state pairs are valid. A rejected guard makes no mutation unless the row expressly defines a durable alternative. Completing, pausing, cancelling or failing never discards observed effects.

| Command | From | To | Required guard |
| --- | --- | --- | --- |
| Validate | Submitted or Blocked with validation return stage | Validated or Blocked | Strict schema and pinned repository and instructions; persist a typed blocker when valid input cannot be resolved |
| Authorize | Validated or AwaitingApproval | Authorized or Recovering | Current explicit matching grant; revalidate a retained matching plan through Recovering; a changed grant requires settled prior work and a new plan from Authorized |
| Plan | Authorized | Planned | Immutable plan, approved outputs, gates and pinned source |
| Queue | Planned | Scheduled | Job and resource policy permit queueing; no worker authority yet |
| Start | Scheduled | Executing | Fresh ownership and live admitted lease, current grant and unchanged plan |
| Verify | Executing | Verifying or AwaitingApproval | Settled execution and a committed verified prefix covering every planned unit for the candidate; the final diff must meet the exact batch gate, or a short final batch requires owner revision |
| Accept | Verifying | Completed | Matching mandatory evidence, required effect receipts and no outstanding obligations |
| Pause | Scheduled, Executing or Verifying | Recovering or Paused | Authorized stop fences worker; Paused requires settled cleanup and effects |
| Resume | Paused or Blocked with recoverable execution context | Recovering | Authorized request and durable plan; restart guards run before dispatch |
| Cancel, Revoke or Fail | Any nonterminal state | Recovering, Cancelled, AwaitingApproval or Failed | Authorized stop or trusted failure records disposition and fences worker; immediate disposition only when no obligations remain |
| RequireReconciliation | Scheduled, Executing or Verifying | Recovering | Trusted evidence of lost ownership, lease expiry or unresolved provider effect; fence the old epoch |
| FinishRecovery | Recovering | Scheduled, Verifying, Blocked, AwaitingApproval, Paused, Failed or Cancelled | Trusted verdict, current revision, authority and verified recovery; unknown effects keep Recovering |

On process or lease loss, the recovery service fences prior ownership and persists Recovering through the same CAS rules. Active states with unresolved old work cannot issue replacement leases. In Recovering a valid newer stop may update the pending disposition. Final recovery applies the pending disposition before authorizing further work. Completed, Failed and Cancelled have no outgoing transitions. Authorized replay of an accepted command returns its receipt and has no new side effects.

## Persistence and effects

Use the [aggregate record contract](../../crates/assignments/specifications/modules/persistence.md). Checkpoints are contiguous under the immutable active plan. Store typed evidence before advertising verified progress. Use live grants, pinned observations and explicit admission for execution. Reconcile uncertain provider operations through [recovery](../../crates/assignments/specifications/modules/recovery.md) before repeating them. An authorized exact count from the [batch contract](../../crates/assignments/specifications/modules/batching.md) governs each seal. Authorization for the reference Vimbai workflow does not change other assignments' counts.

Use the [lifecycle fixtures](../../contracts/acceptance/assignments/lifecycle-fixtures.json) to verify restart at unit 18, 31st-file denial, short-batch review and push/PR reconciliation. Bind release evidence to [requirements](../../REQUIREMENTS.md). Exercise logical reference rules and later qualify the actual provider, storage and runtime adapters.

## Implementing components

- [Assignments](../../crates/assignments/DESIGN.md)
- [Storage](../../crates/storage/DESIGN.md)
- [Governance](../../crates/governance/DESIGN.md)
