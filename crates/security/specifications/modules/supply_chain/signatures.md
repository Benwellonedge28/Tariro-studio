# Package signature policy

**ZIP-SECURITY-SUPPLY-CHAIN-SIGNATURES-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/supply_chain/signatures.rs`

## Boundary and inputs

Accept a versioned artifact envelope, expected package and domain identity, exact artifact and provenance digests, and current signer policy. Use the [signature port](../cryptography/signatures.md) with trusted key enrollment, required purpose and allowed edition. Verify signature validity and signer/authority policy as separate predicates.

## Behavior and failure handling

Reject untrusted or revoked signer, wrong domain, mismatched digests and unsupported mandatory envelope fields. Do not accept unsigned fallback when signature policy requires a signature. Preserve evidence of the exact verified payload and qualification policy without exposing key material.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-SIGNATURES-T01.** Sign an exact synthetic candidate with an untrusted test signer and verify policy denial. Provide the expected signer but changed provenance digest and verify rejection before release qualification.
