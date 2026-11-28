# Egress authorization boundary

**ZIP-SECURITY-DEFENSES-DATA-EXFILTRATION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/defenses/data_exfiltration.rs`

## Boundary and inputs

Bind outbound operation to exact normalized destination identity, purpose, data class, argument and payload scope, and current independent egress grant. Validate target and scoped disclosure before handing any bytes to the transport. Deny unknown classified data or unsupported destination proof.

## Behavior and failure handling

Reapply destination and disclosure checks on every change of target, including redirects. Require the transport to report and enforce actual destination identity, and stop if it cannot. Recheck authorization before dispatch and preserve unresolved transmission under original effect identity on lost receipt. Never perform a network call merely to resolve an unapproved preview.

## Acceptance

**ZIP-SECURITY-DEFENSES-DATA-EXFILTRATION-T01.** Use two local synthetic endpoints in a controlled transport fixture. Decline the destination change when it goes outside scope, verify zero second requests and preserve the original request observation.
