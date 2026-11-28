# Identity failure classes

**ZIP-IDENTITY-ERROR-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/error.rs`

## Boundary and inputs

Define stable typed failure classes for malformed request, unauthenticated proof, expiry, revocation, wrong audience or workspace, stale revision and unavailable issuer. Scope any diagnostic provenance to an authorized observer. Preserve no proof material, secret tokens or unverified external profile content.

## Behavior and failure handling

At unauthorized boundaries map unavailable or concealed principal details to the same public denial as unknown identity. Authenticated scoped diagnostics may distinguish a recoverable adapter outage from an expired session. Ambiguous mutations reconcile under original identity before retry. No diagnostic-driven fallback relaxes a verification rule.

## Acceptance

**ZIP-IDENTITY-ERROR-T01.** Compare public results for absent and concealed principals under unauthorized identities. Verify equal safe denials and no enrollment disclosure. Inject a synthetic secret in an adapter error and confirm redaction.
