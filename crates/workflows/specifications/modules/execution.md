# Fenced workflow execution

**ZIP-WORKFLOWS-EXECUTION-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/execution.rs`

The runner holds a durable workflow run identity, immutable compiled plan and binding revision. Composition injects a workflow journal, scheduler, assignment evidence and governance ports. The scheduler owns job attempt and dispatch retry accounting. Runtime owns execution, teardown and leases. Workflows owns node eligibility and checkpointed semantic results. No new direct Storage or Runtime dependency is required.

| From | Guard or observation | To |
| --- | --- | --- |
| Pending | Dependencies satisfied and stored guard is true | Runnable |
| Pending | Stored guard false | Skipped |
| Pending | Dependency cannot satisfy its edge or guard invalid | Blocked |
| Runnable | Live authority and attempt intent commit | Submitting |
| Submitting | Scheduler confirms the exact job exists | Scheduled |
| Submitting or Scheduled | Ambiguous transition, lost ownership or possible external effect | Recovering |
| Scheduled | Current trusted success after cleanup and verified outputs | Succeeded |
| Scheduled | Settled permanent failure or exhausted retries | Failed |
| Scheduled | Eligible transient failure and scheduler accepts retry | Scheduled |
| Pending or Runnable | Authorized cancellation before submission | Cancelled |
| Submitting, Scheduled or Recovering | Fenced shutdown and settled disposition | Cancelled or Failed |
| Recovering | Exact lookup and settled trusted state | Runnable, Scheduled, Succeeded, Failed or Blocked |
| Succeeded | Separately authorized compensation confirmed | Compensated |

Skipped, Blocked, Cancelled, Failed and Compensated do not reopen through replay. A recovered return to Runnable is possible only when scheduler submission and any effect are conclusively absent and no retry denial applies. No other edges are valid. Persist intent and stable scheduler job identity before submission. An equal retry uses the same job identity. Do not call a capability or enqueue a replacement while submission is unknown. For changed plan or binding revision use a separately authorized run. Event-driven starts deduplicate the authorized trigger identity and compiled revision before creating a run.

Schedule only already eligible nodes. Validate live permissions, conflicts and budget at the scheduler and capability gate. Recheck ownership before recording progress. Persist attempt receipts, verified artifacts and derived readiness through [checkpoint](checkpoint.md). A workflow completes successfully only if every required node and output satisfies its declared contract and no work or effect remains unresolved. Observable statuses preserve partial outcomes. Cancellation fences new dispatch and routes in-flight work to scoped reconciliation.

**ZIP-WORKFLOWS-EXECUTION-T01.** Crash after verification of one independent node. Verify the sibling remains eligible, the durable node never executes again, and a downstream join waits for all required predecessors.
