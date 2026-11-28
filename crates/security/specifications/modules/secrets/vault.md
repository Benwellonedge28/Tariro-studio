# Effect-local secret resolution

**ZIP-SECURITY-SECRETS-VAULT-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/secrets/vault.rs`

## Boundary and inputs

Accept a qualified in-adapter request with exact secret reference, current effect claim, authorized adapter, destination, purpose and epoch. Validate all scope and generation bindings before resolving. Use the shortest approved lifetime to present the secret only to the qualified transport or protocol boundary.

## Behavior and failure handling

Keep resolved material out of snapshots, evidence, diagnostics, caches and model inputs. The adapter owns the material lifetime and disposes of it through qualified cleanup on success, cancellation or failure. No claim is made about buffers outside the approved adapter's ownership. Unavailable secure storage or incompatible destination denies without fallback.

## Acceptance

**ZIP-SECURITY-SECRETS-VAULT-T01.** Use one qualified destination and one different destination with the same reference. Deny the latter before lookup. Cancel the qualified operation and verify no secret bytes are retained in diagnostics or application-owned evidence.
