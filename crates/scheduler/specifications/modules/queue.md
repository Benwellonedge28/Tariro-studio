# Bounded durable job queue

**ZIP-SCHEDULER-QUEUE-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/queue.rs`

Count Waiting, Ready, Reserving, Dispatched, Recovering and RetryWait toward the resolved `scheduler.max_workspace_queue_items`. Terminal and Blocked jobs keep their receipts under retention and do not consume active queue slots. Admission checks and increments the workspace count under the same CAS transaction as first insertion. An identical authorized enqueue replays the stored result without consuming another slot. Reject a different specification for an existing key. When a limit shrinks below current count, stop new inserts and keep all admitted jobs under their existing cancellation rules.

Derive the ready index from committed state and eligible time. Jobs leave the index when Reserving commits. Do not enqueue a second copy for a resource denial or delayed retry. On capacity deferral, record why and which revisions can wake the candidate. Bounded scans must advance a stable continuation across the same snapshot so that a denied first entry cannot hide eligible later entries. Queue caches are advisory. Rebuild from the durable state after restart and verify queue count before dispatch.

**ZIP-SCHEDULER-QUEUE-T01.** With two enqueue calls competing for the last slot, one new job can commit. The loser leaves existing ready jobs, count and journal unchanged. Repeated enqueue of the winning exact specification keeps the count stable.
