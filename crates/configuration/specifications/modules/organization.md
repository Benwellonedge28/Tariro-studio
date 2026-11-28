# Organization policy overlay

**ZIP-CONFIGURATION-ORGANIZATION-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/organization.rs`

## Boundary and inputs

Accept policy only from a trusted installation composition port with verified issuer, scope, revision, validity and digest. Bind the policy to the selected organization and installation before normalization. Reject a stale or different body submitted for the same revision. An exact valid replay of the same verified document is idempotent. Normalize registry allow sets, ceilings, requirements and exact constraints into the typed mandatory domain.

## Behavior and failure handling

Use a trusted validity observation. Invalid or expired replacement data cannot widen a restriction. If the active policy itself expires or loses trust, retain its restrictive evidence and block covered decisions that require fresh authority. No fallback to unconstrained preferences occurs. New policy activates through the Config loader's revision gate. Mandatory effect revocation is independently checked before the effect, including when a configuration reload fails. Never infer external authority from a repository.

## Acceptance

**ZIP-CONFIGURATION-ORGANIZATION-T01.** Send a wrong-organization document, expired replacement and same-revision conflicting body. Verify all fail and preserve restrictions. Expire the active policy and confirm a protected effect stays denied until an authorized replacement is active.
