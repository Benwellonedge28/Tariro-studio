# Authenticated actor context

**ZIP-SECURITY-AUTHENTICATION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/authentication.rs`

## Boundary and inputs

Consume the verified Identity principal context returned by the [authentication contract](../../../identity/specifications/modules/authentication.md). Bind the requesting actor to the exact audience, workspace and enrolled credential or session generations. Require trusted time, verified membership and authenticated transport when selected by policy. Keep raw proof handling inside the qualified Identity or transport adapter.

## Behavior and failure handling

Before requesting permission, verify that context still matches current scope and identity generations. Treat stale or incomplete observations as unauthenticated or unavailable under the typed policy. Never reconstruct trusted context from request DTOs, cached role names or model text. Adapters may expose only the minimal attributable context needed by Security.

## Acceptance

**ZIP-SECURITY-AUTHENTICATION-T01.** Supply one valid context, one wrong-audience context, and a context backed by a retired credential generation. Only the first enters permission evaluation. No denied case reveals membership outside the caller's scope.
