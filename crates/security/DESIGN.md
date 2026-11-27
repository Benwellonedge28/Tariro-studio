# Security crate design

**Contract version** 1.0. Master design §42. Planned implementation.

## Responsibility and dependencies

Evaluate authenticated principal, RBAC, ABAC, capability and revocation. Resolve opaque secrets only inside approved adapter. Redact before persistence or egress.

First-party dependencies: [foundation](../foundation/DESIGN.md), [identity](../identity/DESIGN.md), [storage](../storage/DESIGN.md)

- [Security](../../specifications/2300-security/security.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `decide_access(request)`
- `resolve_secret(reference)`
- `inspect_output(data)`
- `verify_signature()`

Record families: Capability and assurance records, SecretRef, KeyId, signature envelope. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `AuthorizationDecision { decision_id, policy_digest, scope_digest, outcome }`
- `AccessRequest { principal, workspace, operation, target, grant, attributes }`

- `decide_access(request: AccessRequest, trust: &TrustState) -> Result<AuthorizationDecision>`

## Failure, safety and resource limits

Deny overrides allow. Never supply plaintext secrets to prompts, logs or audit. Fail closed if state, clock or key store cannot be validated.

- `Denied`
- `SecretUnavailable`
- `Revoked`
- `IntegrityFailure`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/security/src/
├── lib.rs
├── error.rs
├── threat_model.rs
├── authentication.rs
├── authorization.rs
├── secrets/
│   ├── mod.rs
│   ├── vault.rs
│   ├── keyring.rs
│   ├── rotation.rs
│   └── redaction.rs
├── cryptography/
│   ├── mod.rs
│   ├── hashing.rs
│   ├── encryption.rs
│   ├── signatures.rs
│   ├── key_management.rs
│   └── random.rs
├── permissions/
│   ├── mod.rs
│   ├── rbac.rs
│   ├── abac.rs
│   ├── capability.rs
│   ├── inheritance.rs
│   └── revocation.rs
├── defenses/
│   ├── mod.rs
│   ├── prompt_injection.rs
│   ├── command_injection.rs
│   ├── data_exfiltration.rs
│   ├── dependency_risk.rs
│   └── secret_leakage.rs
├── supply_chain/
│   ├── mod.rs
│   ├── sbom.rs
│   ├── provenance.rs
│   ├── signatures.rs
│   └── verification.rs
└── incident_response.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test prompt injection boundaries, secret canaries and delegated capability attenuation.
