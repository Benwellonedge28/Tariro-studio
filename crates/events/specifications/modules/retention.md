# Contiguous retention and replay boundary

**ZIP-EVENTS-RETENTION-001 · v1.1 candidate · Owner** Events maintainers

**Planned source** `crates/events/src/retention.rs`

Compute a proposed floor from versioned policy, required consumer checkpoint protection, audit and backup pins, unsettled processing and dead-letter dependencies. Only remove a contiguous prefix ending at or before all protected limits. Before advancing past an ordinary consumer, verify a scoped snapshot covering the proposed floor exists. Expiration of unprotected consumers is permitted only by policy. Required consumers block their protected prefix until checkpoint or authorized recovery.

Compare the stream head, current floor and protection revisions inside the Storage writer. In one bounded transaction delete an eligible prefix chunk, decrement referenced object counts and update the floor. Retain the stream head and producer identity fence independent of the pruned rows. Preserve required consumer receipt protection until replay becomes impossible. Failed or ambiguous prune commits require reconciliation before repeating. Readers see either full pre-prune state or full post-prune state. Iterate in bounded chunks without exposing gaps.

**ZIP-EVENTS-RETENTION-T01.** A pinned event blocks clearing its prefix. Advance the floor after authorized release with a verified snapshot. Confirm a cursor below the floor expires while one at the floor resumes normally.
