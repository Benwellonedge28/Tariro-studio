# Supervisor restart and fencing

**ZIP-RUNTIME-RECOVERY-CRASH-RECOVERY-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate.

**Planned source:** `crates/runtime/src/recovery/crash_recovery.rs`

## Recovery entry and ownership

This module runs the crate-private startup pass over open attempt records from the [supervisor](../supervisor.md). It receives owned recovery context from composition, including a storage handle, supervised platform observer, resource cleanup verifier, and effect-specific readers limited to the recorded intent. It returns a typed runtime failure when the journal cannot be trusted. Individual unresolved attempts remain visible with their durable disposition and evidence.

1. Validate store version and integrity. Acquire exclusive local recovery ownership using storage revision checks. A supervisor unable to confirm ownership keeps intake closed. Within each recovered record, increment the runtime owner generation with checked arithmetic, set RecoveryRequired and fence the old worker. Deny on overflow and preserve the record. The resource manager independently fences outstanding leases and accepts only current cleanup authority.
2. Look up the durable locator in the exact platform adapter. If unknown or inconsistent, retain the hold and block that task. If live, move to Cancelling and stop the contained work under cleanup authority. If conclusively absent, recover authoritative teardown and metering evidence. Never reattach an old worker or reopen its launch gate.
3. Read accepted checkpoints as a contiguous, verified prefix. Retain the last valid predecessor for retry. Missing required evidence blocks the affected resume and records the reason. An interrupted checkpoint write is decided by its storage receipt even when its notification was lost.
4. Resolve outstanding external intent using [reconciliation](reconciliation.md). Inspect resource release in its owning journal. If release already committed, use the original receipt. If it is still pending, reissue the cleanup transaction with the same proof only while that proof remains current, or obtain a fresh proof under the current cleanup epoch. A packet timeout or expired execution lease supplies no proof of absence.
5. Finalize in one runtime transaction when prerequisites are satisfied. Prefer a previously committed terminal outcome on replay. Otherwise apply the verified receipt or recorded disposition. If verified absence and no durable result remain after an interruption, record Failed with the interruption cause. A successor requires observed release, a terminal predecessor outcome classified safe to retry, a fresh live grant, scheduler budget and a new explicit attempt identity. Cancellation and domain denial alone are never retried automatically.

Follow resolved transaction and operation budgets. Repeated recovery does not duplicate stage results, release, or events. A corrupt or incompatible journal blocks intake globally. An adapter or effect uncertainty with intact indexes blocks the affected task and preserves its accounted occupancy. Design-time conformance does not qualify actual restart behavior on a platform.

## Acceptance

**ZIP-RUNTIME-RECOVERY-CRASH-RECOVERY-T01.** Interrupt after child creation, before checkpoint commit, after checkpoint commit, and after terminal commit with a lost reply. Confirm that old generations cannot publish, only durable checkpoints are restored and the terminal event exists once after replay. See [fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json).
