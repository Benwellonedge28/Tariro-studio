# Durable principal or session fencing

**ZIP-IDENTITY-REVOCATION-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/revocation.rs`

## Boundary and inputs

Accept a separately authorized revoke command for the exact principal, enrollment or session and expected generation. Advance the target's checked epoch and commit the redacted intent with its event in the owning transaction. Preserve durable generation updates before notifications. Replay exact command identity without another advance.

## Behavior and failure handling

Gate future authentication and effects on current applicable principal, membership and session epochs. Race revocation against the authoritative effect claim. If revocation commits first, no old identity can claim. Previously claimed effects remain attributable and reconcile at their owning boundary. Restart reads the durable epoch and does not recreate privileges from a cached context.

## Acceptance

**ZIP-IDENTITY-REVOCATION-T01.** Race logout with a new action, restart after the revoke transaction and before notification, then attempt old-session replay. Verify no new old-epoch effect can claim and historical receipt remains accessible in scope.
