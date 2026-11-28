# Qualified entropy abstraction

**ZIP-SECURITY-CRYPTOGRAPHY-RANDOM-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/cryptography/random.rs`

## Boundary and inputs

Expose a bounded fill operation through an enrolled cryptographic entropy source for production. The caller supplies an admitted buffer, declared purpose and qualified adapter. Separate deterministic test construction so production keys and nonces cannot use a seeded test fixture.

## Behavior and failure handling

Fail if the source is unavailable or returns incomplete output. Never fill remaining bytes from clocks, identifiers or application state. Keep a partial result private and unusable. Retry only through the qualified source under the calling operation's bounds. Entropy errors and diagnostics disclose no buffer contents.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-RANDOM-T01.** Have a synthetic source fail before filling and after a partial fill. Neither produces usable randomness or a fallback call. Verify test-only deterministic construction cannot qualify a production provider.
