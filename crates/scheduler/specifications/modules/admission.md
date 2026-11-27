# Schedule-time scope and capacity guard

**ZIP-SCHEDULER-ADMISSION-001 · v1.1 candidate · Owner** Scheduler maintainers

**Planned source** `crates/scheduler/src/admission.rs`

Build the Resources request from the immutable job and the stored Reserving intent. Use the exact assignment, task and attempt number and the current verified principal and workspace relation. Fetch the current capacity revision. Compute the earliest valid local deadline per [deadline](deadline.md), then call the [resource admission port](../../../resources/specifications/modules/admission.md) outside any scheduler transaction. At handoff verify the lease matches the attempt and its live authority. Runtime independently checks the claim, lease and authority at execution.

A capacity shortage or stale measurement is a deferred scheduling condition only if Resources definitively committed no lease. Park the candidate until relevant observable capacity, policy or clock state changes. When reserve commits but the scheduler no longer owns the candidate, reconcile or obtain authorized cleanup proof and release by assignment and attempt key. A process death, request timeout or ambiguous response is insufficient proof of no lease. Persist Recovering and fence the attempt. Never dispatch a later attempt until the original accounting and any possible runtime dispatch settle.

**ZIP-SCHEDULER-ADMISSION-T01.** Revoke during reserve and verify zero runtime handoffs. Resolve and return the unused hold only with current proof. Repeat with a lost reserve response and verify recovery can find the original attempt from the persisted intent.
