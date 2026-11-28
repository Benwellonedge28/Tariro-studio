# Opaque key lifecycle

**ZIP-SECURITY-CRYPTOGRAPHY-KEY-MANAGEMENT-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/cryptography/key_management.rs`

## Boundary and inputs

Bind a key reference to approved algorithm, owner, protection domain, purpose, generation, effective validity and lifecycle state. Separate active, retired and revoked generations. Resolve operations through the qualified key adapter and never return key material to general application state. [NIST key-management guidance](https://csrc.nist.gov/Projects/Key-Management/key-management-guidelines)

## Behavior and failure handling

Require live purpose and generation checks before every new use. A retired generation may verify or decrypt historical material only under explicit policy and qualified ownership. A revoked generation cannot produce new protected material. Stage rotation, prove readiness and publish under expected revision, keeping external ambiguity tied to the original operation. Destruction requires separate retention and recovery checks.

## Acceptance

**ZIP-SECURITY-CRYPTOGRAPHY-KEY-MANAGEMENT-T01.** Reject a key used for a different purpose, a stale generation and a newly revoked signing key. Verify a historical verification path is allowed only when policy expressly permits it.
