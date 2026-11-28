# Security crate design

**Contract version** 1.1 candidate. Master design §42. Planned implementation.

## Responsibility and dependencies

Consume a verified Identity context and evaluate exact scoped role, attribute, capability and revocation inputs. Governance and the owning adapter check current bindings at effect claim and dispatch. Resolve opaque secrets only inside approved adapters. Redact before persistence or egress.

First-party dependencies: [foundation](../foundation/DESIGN.md), [identity](../identity/DESIGN.md), [storage](../storage/DESIGN.md)

- [Security](../../specifications/2300-security/security.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `decide_access(request)`
- `resolve_secret(reference)`
- `inspect_output(data)`
- `verify_signature()`

Record families: capability and assurance records, SecretRef, KeyId and signature envelope. The [permission boundary](specifications/modules/permissions/mod.md) coordinates evidence. The [secrets boundary](specifications/modules/secrets/mod.md) exposes scoped references and keeps resolved material within an approved adapter lifetime. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

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

## Planned source-file contracts

The entries below specify file ownership and stable acceptance cases. See the [requirements map](../../contracts/requirements/modules/security.json). The cryptography, defensive controls, supply-chain and incident response drafts remain open along with concrete adapter qualification and independent review.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`threat_model.rs`](specifications/modules/threat_model.md)
- [`authentication.rs`](specifications/modules/authentication.md)
- [`authorization.rs`](specifications/modules/authorization.md)
- [`secrets/mod.rs`](specifications/modules/secrets/mod.md)
- [`secrets/vault.rs`](specifications/modules/secrets/vault.md)
- [`secrets/keyring.rs`](specifications/modules/secrets/keyring.md)
- [`secrets/rotation.rs`](specifications/modules/secrets/rotation.md)
- [`secrets/redaction.rs`](specifications/modules/secrets/redaction.md)
- [`cryptography/mod.rs`](specifications/modules/cryptography/mod.md)
- [`cryptography/hashing.rs`](specifications/modules/cryptography/hashing.md)
- [`cryptography/encryption.rs`](specifications/modules/cryptography/encryption.md)
- [`cryptography/signatures.rs`](specifications/modules/cryptography/signatures.md)
- [`cryptography/key_management.rs`](specifications/modules/cryptography/key_management.md)
- [`cryptography/random.rs`](specifications/modules/cryptography/random.md)
- [`permissions/mod.rs`](specifications/modules/permissions/mod.md)
- [`permissions/rbac.rs`](specifications/modules/permissions/rbac.md)
- [`permissions/abac.rs`](specifications/modules/permissions/abac.md)
- [`permissions/capability.rs`](specifications/modules/permissions/capability.md)
- [`permissions/inheritance.rs`](specifications/modules/permissions/inheritance.md)
- [`permissions/revocation.rs`](specifications/modules/permissions/revocation.md)
- [`defenses/mod.rs`](specifications/modules/defenses/mod.md)
- [`defenses/prompt_injection.rs`](specifications/modules/defenses/prompt_injection.md)
- [`defenses/command_injection.rs`](specifications/modules/defenses/command_injection.md)
- [`defenses/data_exfiltration.rs`](specifications/modules/defenses/data_exfiltration.md)
- [`defenses/dependency_risk.rs`](specifications/modules/defenses/dependency_risk.md)
- [`defenses/secret_leakage.rs`](specifications/modules/defenses/secret_leakage.md)
- [`supply_chain/mod.rs`](specifications/modules/supply_chain/mod.md)
- [`supply_chain/sbom.rs`](specifications/modules/supply_chain/sbom.md)
- [`supply_chain/provenance.rs`](specifications/modules/supply_chain/provenance.md)
- [`supply_chain/signatures.rs`](specifications/modules/supply_chain/signatures.md)
- [`supply_chain/verification.rs`](specifications/modules/supply_chain/verification.md)
- [`incident_response.rs`](specifications/modules/incident_response.md)
