# Agent failure vocabulary

**ZIP-AGENTS-ERROR-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/error.rs`

## Boundary and inputs

Provide stable agent errors CapabilityDenied, InvalidRole, MailboxFull, AgentStopped, DelegationLimit, LeaseLost, Cancelled, UnsupportedModel, Conflict and OutcomeUnknown. Carry only operation class and permitted scoped evidence. Preserve diagnostic provenance without raw grants, source payloads, model responses or security tokens.

## Behavior and failure handling

Validate shape and authority before returning membership or state details. For a scoped replay distinguish an exact committed receipt, conflicting request and unresolved disposition. Then check lifecycle, binding and relevant capacity. OutcomeUnknown requires reconciliation and never communicates successful delegation or execution. A cancellation signal leaves previously verified effects intact. Retry only at the owning documented idempotent boundary.

## Acceptance

**ZIP-AGENTS-ERROR-T01.** Fill the mailbox, simulate an uncertain effect and deliver a stale outcome under authorized scope. Assert separate stable error codes, no false success and no leaked private payload in diagnostics.
