# Audience-bound session

**ZIP-IDENTITY-SESSION-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/session.rs`

## Boundary and inputs

Bind opaque SessionId to verified principal, workspace, registered audience and qualified device or channel where required. Record issued and expiry times, principal and session generations and the bound membership revision. SessionId is a lookup reference and is never accepted as bearer authentication. Resolve receives trusted presentation and time evidence through composition.

## Behavior and failure handling

Require live proof, matched audience and workspace, active membership and current epochs. Use a trusted start-inclusive, expiry-exclusive window. Missing or uncertain observations fail closed. Logout commits the durable fence before notification. Store no bearer material or recoverable authentication bytes in the record. After restart verify both record and current evidence.

## Acceptance

**ZIP-IDENTITY-SESSION-T01.** Check exact expiry, cross-audience lookup and mismatched workspace. All deny without disclosure. Race logout with resolve before a protected operation and verify the next effect checks the current epoch again.
