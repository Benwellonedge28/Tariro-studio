# Authenticated data protection

**ZIP-SECURITY-CRYPTOGRAPHY-ENCRYPTION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/cryptography/encryption.rs`

## Boundary and inputs

Accept bounded input and a qualified authenticated-encryption suite for the expected protection domain. Bind storage edition, workspace, object identity and required header fields in associated data. The owning key adapter supplies the approved nonce lifecycle and proves per-key uniqueness for the selected nonzero-nonce suite, including across writers and recovery. [RFC 5116](https://www.rfc-editor.org/rfc/rfc5116.html)

## Behavior and failure handling

Validate envelope shape, suite, identity and bounds before key use. Verify the entire authenticated unit before making plaintext available to its scoped consumer. Reject modified headers, truncation or bound-domain mismatches without releasing plaintext. If nonce safety cannot be confirmed after interrupted allocation or restore, suspend new encryption with that key until qualified recovery or rotation.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-ENCRYPTION-T01.** Open an intact synthetic object in its approved workspace. Change workspace, nonce binding, header and ciphertext independently and verify no plaintext is delivered. Restart with an unavailable nonce allocator and confirm sealing stays blocked.
