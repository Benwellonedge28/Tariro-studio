# Opaque secret-reference boundary

**ZIP-SECURITY-SECRETS-MOD-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/secrets/mod.rs`

## Boundary and inputs

Define SecretRef as an opaque scoped address with validated owner, credential generation and approved adapter binding. Expose [vault](vault.md), [keyring](keyring.md), [rotation](rotation.md) and [redaction](redaction.md) operations through their designated interfaces. SecretRef can be persisted only where its metadata is appropriate for the audience.

## Behavior and failure handling

Keep resolved material in private adapter-lifetime types with no general display, debug, clone or serialization surface. Use separate typed references and live authority at resolution. Construction, hashing or serialization of the reference does not retrieve a secret or indirectly encode its bytes. External use remains destination- and action-bound.

## Acceptance

**ZIP-SECURITY-SECRETS-MOD-T01.** Serialize an authorized reference and inspect raw serialized bytes and debug output for a synthetic value. Verify retrieval requires the private adapter path and a live scoped request.
