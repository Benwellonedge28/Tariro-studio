# Controlled draining

**ZIP-SCHEDULER-PREEMPTION-001 · v1.1 · Owner:** Scheduler maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/scheduler/src/preemption.rs`

## Boundary and inputs

Accept a live preemption policy decision naming the exact attempt, claim epoch, reason and approved control action. Prefer a verified safe boundary when the operation allows it. Use supervisor drain or cancellation under the owning authority. The Scheduler records fencing and recovery intent, while Runtime owns process containment and release evidence.

## Behavior and failure handling

Authorize before requesting control. Serialize racing preemption and finish using the Scheduler CAS. A receipt committed first remains final. A fence committed first disables old worker settlement and requires trusted reconciliation. Preserve durable checkpoints and accepted external effect receipts. No replacement starts while release or effect settlement is ambiguous. An old or repeated command grants no additional retry, time or resource credit.

## Acceptance

**ZIP-SCHEDULER-PREEMPTION-T01.** Preempt while a verified effect receipt is committed and then drop the control response. Verify the original receipt persists, the old worker cannot settle scheduler state, and replacement remains blocked until reconciliation under the original intent.
