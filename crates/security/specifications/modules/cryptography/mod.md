# Versioned cryptographic ports

**ZIP-SECURITY-CRYPTOGRAPHY-MOD-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/cryptography/mod.rs`

## Boundary and inputs

Expose typed suite and algorithm tags, opaque key references, and separate hashing, authenticated encryption, signature and entropy ports. Dispatch against the reviewed registry for the request's format, domain and purpose. Reject unknown or disabled algorithms before selecting a key or allocating a payload buffer.

## Behavior and failure handling

Validate bounds, compatible key usage and version, then dispatch to a qualified provider. A provider failure returns a typed error without trying a weaker or caller-selected fallback. Keep provider names and concrete key handles out of public records. Changes to supported suites require independent compatibility, key migration and provider qualification evidence.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-MOD-T01.** Submit a supported suite, an unknown tag, and a known suite disabled by policy. Only the supported allowed input may reach the provider, and no case loads an unrelated key.
