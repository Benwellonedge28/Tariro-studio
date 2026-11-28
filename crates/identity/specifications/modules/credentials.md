# Opaque credential references

**ZIP-IDENTITY-CREDENTIALS-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/credentials.rs`

## Boundary and inputs

Expose CredentialRef as an opaque owner- and adapter-scoped locator with identity, namespace and expected generation, validated against the trusted registry. It is permitted as metadata only where the consumer is authorized to see that scope. It conveys no bearer proof or lookup authority.

## Behavior and failure handling

Persist only scoped reference metadata in Identity. Secret retrieval and use stay in the approved Security adapter with effect, destination and epoch validation. Omit actual credential values from diagnostics, sessions, audit, and serialization. A stale reference remains attributable but cannot activate a retired credential generation.

## Acceptance

**ZIP-IDENTITY-CREDENTIALS-T01.** Serialize scoped principals and session views and scan for synthetic bearer canaries. Substitute a reference from another adapter and verify it cannot enter an authenticated binding.
