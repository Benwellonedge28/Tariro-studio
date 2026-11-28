# Security error vocabulary

**ZIP-SECURITY-ERROR-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/error.rs`

## Boundary and inputs

Define scoped stable security codes for unauthenticated, denied, revoked, expired, secret unavailable, integrity failure and unsupported control. Preserve internal cause distinctions under independently authorized diagnostics. Never attach raw auth inputs, secret values, provider error fields or details from an unauthorized target.

## Behavior and failure handling

For unauthenticated or unauthorized requests, map absent and concealed resources to the same public denial. A failed required control blocks the operation and cannot select a weaker fallback. Distinguish verified pre-effect denial from unresolved outcome in the owning effect journal. Diagnostics must not authorize recovery or retry.

## Acceptance

**ZIP-SECURITY-ERROR-T01.** Compare public errors for unauthorized requests to an absent and a concealed resource. Ensure equal safe outputs. Include a synthetic credential canary in a failing adapter response and verify it is not returned or logged.
