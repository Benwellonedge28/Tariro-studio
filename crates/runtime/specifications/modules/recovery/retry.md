# Budgeted retry classification

**ZIP-RUNTIME-RECOVERY-RETRY-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/recovery/retry.rs`

## Boundary and inputs

Runtime owns a pure predecessor classification after the supervisor establishes trustworthy terminal disposition and confirmed occupancy release. Return EligibleForScheduler only for a definitive transient result or verified interruption with retry-safe effect evidence under the [reconciliation contract](reconciliation.md). Return Blocked while release, effect or evidence is unknown or conflicts with the recorded intent. Return Ineligible for permanent failure, explicit cancellation, authorization denial or incompatible intent. A verified previously successful effect must be retained and only an independently authorized same-identity replay can use it.

## Behavior and failure handling

Do not consume attempts, choose backoff or wake jobs here. The [Scheduler retry contract](../../../../scheduler/specifications/modules/retry.md) owns those decisions under current policy and monotonic deadline. A qualified successor requires new attempt identity, current claim and resource grant. Preserve the prior disposition as input evidence. A classification replay writes no new attempt, release or provider effect.

## Acceptance

**ZIP-RUNTIME-RECOVERY-RETRY-T01.** Feed reconciliation states Unknown, Conflict and definitive Absent after the same transient transport observation. Unknown and Conflict block. Definitive absence plus a terminal released predecessor permits scheduler reevaluation subject to the live deadline. Repeat with cancelled and released predecessor and verify ineligible.
