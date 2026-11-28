# Failure and cleanup owner

**ZIP-AGENTS-SUPERVISION-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/supervision.rs`

## Boundary and inputs

Own the agent-side tracking of accepted runtime attempts, expected epochs and pending effects. Observe the [Runtime supervisor](../../../runtime/specifications/modules/supervisor.md) for verified teardown and resource settlement. Actor lifecycle and agent-owned mailbox handling remain separate from Runtime's authority over process trees and leases.

## Behavior and failure handling

Close new admissions on revoke or stop, fence stale publication, and request cooperative drain through the authorized Runtime path. Preserve all accepted evidence and reconcile lost responses under original attempt identity. A released handle or timeout does not establish teardown. The owner accounts for unsettled resources until verified cleanup. Only confirmed settlement permits a successor.

## Acceptance

**ZIP-AGENTS-SUPERVISION-T01.** Inject agent revocation with an unreaped synthetic child and a stale result. Verify no new effect or accepted progress, a retained resource hold and a Draining agent. Supply valid teardown and observe one recorded settlement.
