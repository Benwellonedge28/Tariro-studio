# Authentication proof binding

**ZIP-IDENTITY-AUTHENTICATION-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/authentication.rs`

## Boundary and inputs

Accept bounded proof presentation plus expected issuer, relying audience, workspace and binding challenge or authenticated transport context. Resolve the configured verifier by trusted local configuration. Verify proof integrity, live issuer key/trust state, claims, freshness and enrollment under one coherent snapshot. Reject unrecognized proof editions and protect the opaque presentation.

## Behavior and failure handling

For a one-use proof, store its consumed identity together with any session issuance under a revision check. An exact replay never issues another session or re-exposes bearer material. Bind transport-backed proof to the verified endpoint and channel using the enrolled adapter. Unsupported provider, missing proof or stale enrollment denies without alternate verifier fallback.

## Acceptance

**ZIP-IDENTITY-AUTHENTICATION-T01.** Replay a proof for a different workspace and then for a different audience. Verify both deny without session writes. Race two valid same-proof requests and confirm at most one new session record.
