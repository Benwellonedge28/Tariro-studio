# Scoped incident lifecycle

**ZIP-SECURITY-INCIDENT-RESPONSE-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/incident_response.rs`

## Boundary and inputs

Accept a scoped incident report with verified or unresolved evidence, affected capabilities and authenticated response authority. Persist the incident before notification. Use the owning Governance stop and Identity revocation paths to fence future effects, while keeping independent allowed scopes available where policy permits.

## Behavior and failure handling

Keep affected intake closed after restart. Preserve redacted evidence and reconcile previously claimed effects under original identities. Any restoration requires current qualified controls, reviewed recovery evidence and a separately authorized operation. Closing an incident does not reactivate fenced grants. Evidence retention and disclosure remain separately authorized.

## Acceptance

**ZIP-SECURITY-INCIDENT-RESPONSE-T01.** Crash after a scoped stop and before notifying a worker. Reload with the capability still paused, reconcile a committed effect and verify reopening requires a fresh authorized decision.
