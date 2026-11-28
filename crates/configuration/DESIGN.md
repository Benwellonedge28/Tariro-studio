# Configuration crate design

**Contract version** 1.2 candidate. Master design §10. Planned implementation.

## Responsibility and dependencies

Apply deterministic defaults, profile, user, workspace, environment allowlist and explicit flags in order. Apply mandatory policy by intersection. Replace arrays atomically. Resolve and validate before activation.

First-party dependencies: [foundation](../foundation/DESIGN.md)

- [Resources](../../specifications/0300-resources/resources.md)

## API and data

The public resolution operation uses this Rust-shaped pseudocode.

```rust
pub fn resolve(
    layers: &[ConfigLayer],
    mandatory: &PolicyConstraints,
) -> Result<ResolvedConfig, ConfigError>;
```

`ConfigLayer` is an authorized normalized input with source class, source digest, edition and typed values. `PolicyConstraints` is the normalized mandatory domain derived from verified policy inputs. `ResolvedConfig` exposes effective typed values, active provenance and tagged configuration and policy digests without mutable access. [Schema](specifications/modules/schema.md) owns key and value types. [Errors](specifications/modules/error.md) owns `ConfigError`. The resolver borrows its inputs and returns an owned candidate without publishing it. It applies [precedence](specifications/modules/overrides.md) and [validation](specifications/modules/validation.md). Treat effective values and contributing origins as one indivisible generation. The [profile registry](specifications/modules/profiles/mod.md) separates explicit preferences from derivation markers. [Security](specifications/modules/security.md) and [inference](specifications/modules/inference.md) project typed preferences and requirements without acquiring execution or network authority.

[Loader](specifications/modules/loader.md) owns explicit bounded I/O and compare-and-swap activation. [Defaults](specifications/modules/defaults.md) and [migration](specifications/modules/migration.md) own base schema edition handling. Preserve original bytes and use a verified release baseline as the sole source of the added drain setting during v1 upgrade. Scope, parsing and migration are verified before merge. Neither a local preference nor a previously activated snapshot confers live permission for protected effects.

## Failure, safety and resource limits

Apply the resolved `configuration.max_layer_bytes` to each layer after bounded bootstrap. Reject unknown editions, unknown or duplicate keys, unavailable references required for the profile and unsafe override attempts. No secret payload crosses Configuration. Keep a prior valid immutable generation on failed reload and apply current mandatory revocation independently.

- `InvalidConfig`
- `UnsupportedSchema`
- `PolicyConflict`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/configuration/src/
├── lib.rs
├── error.rs
├── schema.rs
├── loader.rs
├── parser.rs
├── defaults.rs
├── environment.rs
├── overrides.rs
├── validation.rs
├── migration.rs
├── profiles/
│   ├── mod.rs
│   ├── minimal.rs
│   ├── lightweight.rs
│   ├── standard.rs
│   ├── workstation.rs
│   ├── server.rs
│   └── distributed.rs
├── user.rs
├── project.rs
├── organization.rs
├── security.rs
├── inference.rs
└── resources.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Permute unordered inputs and obtain identical digests. Verify a project cannot enable network against an offline policy. Exercise v1 and v2 base defaults and the installation deadline binding with the [drain policy fixtures](../../contracts/acceptance/runtime/drain-policy-fixtures.json). Qualify the concrete canonical snapshot codec and the Rust composition signatures before independent sign-off.

## Planned source-file contracts

The entries below specify file ownership and acceptance. Each contract carries its maturity status. The [requirements map](../../contracts/requirements/modules/configuration.json) associates planned paths with acceptance identifiers. Every planned Configuration source path now has a candidate file contract. Lightweight and standard still need registered installable profile definitions before those options can be activated. Concrete codec, adapter qualification and independent design review remain open.

- [`lib.rs`](specifications/modules/lib.md)
- [`error.rs`](specifications/modules/error.md)
- [`schema.rs`](specifications/modules/schema.md)
- [`loader.rs`](specifications/modules/loader.md)
- [`parser.rs`](specifications/modules/parser.md)
- [`defaults.rs`](specifications/modules/defaults.md)
- [`environment.rs`](specifications/modules/environment.md)
- [`overrides.rs`](specifications/modules/overrides.md)
- [`validation.rs`](specifications/modules/validation.md)
- [`migration.rs`](specifications/modules/migration.md)
- [`profiles/mod.rs`](specifications/modules/profiles/mod.md)
- [`profiles/minimal.rs`](specifications/modules/profiles/minimal.md)
- [`profiles/lightweight.rs`](specifications/modules/profiles/lightweight.md)
- [`profiles/standard.rs`](specifications/modules/profiles/standard.md)
- [`profiles/workstation.rs`](specifications/modules/profiles/workstation.md)
- [`profiles/server.rs`](specifications/modules/profiles/server.md)
- [`profiles/distributed.rs`](specifications/modules/profiles/distributed.md)
- [`user.rs`](specifications/modules/user.md)
- [`project.rs`](specifications/modules/project.md)
- [`organization.rs`](specifications/modules/organization.md)
- [`security.rs`](specifications/modules/security.md)
- [`inference.rs`](specifications/modules/inference.md)
- [`resources.rs`](specifications/modules/resources.md)
