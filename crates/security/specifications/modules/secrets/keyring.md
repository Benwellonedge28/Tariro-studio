# Platform keyring integration

**ZIP-SECURITY-SECRETS-KEYRING-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/secrets/keyring.rs`

## Boundary and inputs

Accept an opaque reference and approved backend binding scoped to tenant, owner, adapter and generation. Probe a qualified platform secure store through the enrolled provider. Check backend identity, expected scope and availability before lookup. Return only authorized in-adapter access or typed unavailability.

## Behavior and failure handling

If the required backend fails or becomes locked, block the affected effect. Never create diagnostic plaintext copies, token files or environment fallbacks. No cross-account or cross-backend lookup without a separately approved binding. Adapter diagnostics must omit identifiers outside authorized scope and omit secret data entirely.

## Acceptance

**ZIP-SECURITY-SECRETS-KEYRING-T01.** Disable the required synthetic keyring and inspect all file and diagnostic writes. Confirm no plaintext fallback, no external call using unavailable credentials and an explicit unavailable disposition.
