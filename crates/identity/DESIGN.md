# Identity crate design

**Contract version** 1.0. Master design §11. Planned implementation.

## Responsibility and dependencies

Resolve authenticated OS user for local IPC or a verified external identity for remote access. Bind session to principal, device and workspace. Persist revocation before notification.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md)

- [Security](../../specifications/2300-security/security.md)
- [Governance](../../specifications/2400-governance/governance.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `authenticate(presentation)`
- `resolve(session)`
- `revoke(session_id)`

Record families: Principal, workspace membership, Session, CredentialRef and revocation epoch. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `Session { id, principal_id, workspace_id, issued_at, expires_at, audience, revocation_epoch }`
- `CredentialRef { namespace, key_id }`

- `resolve(session: SessionId, audience: Audience, now: Timestamp) -> Result<PrincipalContext>`

## Failure, safety and resource limits

Never persist bearer secrets in identity tables. Expired sessions and removed memberships fail closed. Session credentials are audience-bound.

- `Unauthenticated`
- `SessionExpired`
- `Revoked`
- `WorkspaceMismatch`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/identity/src/
├── lib.rs
├── error.rs
├── principal.rs
├── user.rs
├── agent.rs
├── service.rs
├── device.rs
├── organization.rs
├── workspace.rs
├── session.rs
├── authentication.rs
├── credentials.rs
├── federation.rs
├── delegation.rs
├── revocation.rs
└── registry.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test cross-workspace access, logout races and revocation persistence.
