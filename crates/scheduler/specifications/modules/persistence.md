# Schedule and attempt durability

**ZIP-SCHEDULER-PERSISTENCE-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/persistence.rs`

## Records and transactions

Store schema version 1 for each job, attempt, ready index, workspace count, fairness cursor and receipt. Job keys are assignment and task UUIDs; attempt keys append the nonzero attempt number. Record scope, plan and canonical spec digest, immutable dependency edges, current state, revision, latest attempt, charged dispatch count, deadline basis and eligibility delay. Attempt rows record resource request digest, claim epoch, binding and observed result, fence state and receipt references. Use canonical stable state tags and encode unsigned counters as canonical decimal strings in JSON; store typed identifiers in their declared field context. Index current job state by workspace and stable enqueue ordinal, reverse dependencies by prerequisite, and unresolved attempts by job key. Receipt comparisons use attempt identity and digest.

Commit queue count, ready key, claim epochs and required event intents atomically with each applicable state transition. Use checked generation, event and enqueue ordinals. Handlers perform authorization before any read and validate a CAS revision under the transaction. Publish only committed outbox entries. Replays use the same event identity and do not insert extra effects. Unknown storage commit stays unresolved until the journal can prove its disposition. The runtime and resource journals are external to this transaction, so the scheduler holds an intent before calling either and reconciles by the matching attempt.

## Restart and migration

On startup validate schema, record uniqueness and queue counts before opening intake. Rebuild bounded indexes from durable rows. Reconcile Reserving, Dispatched and Recovering rows against both resource occupancy and runtime observations. Claim recovery ownership transactionally before accepting evidence. Treat missing or unavailable facts as unknown. Prove absence or settle work and fence older owners before allowing a replacement attempt. Preserve ledger receipts and committed effect records after restart. Migrations run through the storage migration policy and preserve monotonic high-water counters and unresolved intents.

**ZIP-SCHEDULER-PERSISTENCE-T01.** Stop the scheduler after writing the attempt intent and again after receiving an ambiguous reserve reply. Restart and verify the original key is used for reconciliation and only one live claim epoch can own a job.
