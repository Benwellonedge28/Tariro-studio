# Explicit external identity negotiation

**ZIP-IDENTITY-FEDERATION-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/federation.rs`

## Boundary and inputs

Bind a qualified external issuer, exact subject identifier, supported protocol edition, audience and explicit local enrollment mapping. The mapping belongs to the trusted Identity registry. Never join accounts by display name, email or subject string across issuers. Validate current trust before using an enrolled mapping.

## Behavior and failure handling

Reject issuer drift, stale or missing trust evidence and mismatched audience. Unknown qualified subjects require the deliberate local enrollment path before access. Disable unavailable federated authentication without falling back to another issuer or impairing independently authorized local mechanisms. Reconcile same-revision mapping replacements before allowing new sessions.

## Acceptance

**ZIP-IDENTITY-FEDERATION-T01.** Supply the same subject under two configured issuers, with only the first enrolled. Reject the second even if profile fields match. Pin a different audience and verify the original proof cannot establish that context.
