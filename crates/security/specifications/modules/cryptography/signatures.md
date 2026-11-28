# Domain-bound signature verification

**ZIP-SECURITY-CRYPTOGRAPHY-SIGNATURES-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/cryptography/signatures.rs`

## Boundary and inputs

Verify the registered signature envelope, declared domain, version, signing purpose, canonical message bytes and exact expected artifact digest. Resolve trusted key identity and generation for that domain under the pinned policy and authenticated clock observation. Do not infer trust from the key supplied inside the envelope.

## Behavior and failure handling

Reject unsupported algorithms, unknown keys, mismatch of domain or bytes, and stale or revoked trust when policy requires current qualification. A verified signature proves only the exact registered assertion. Permission to execute, publish or inspect still uses the separate owning gate. Keep evidence bound to signer, verification policy and candidate.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-SIGNATURES-T01.** Verify a valid synthetic signature for the intended domain, then supply it to a different package purpose and a replaced artifact. The latter two fail even though the original signature remains valid.
