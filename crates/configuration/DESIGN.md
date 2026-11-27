# Configuration crate design

**Contract version** 1.0. Master design §10. Planned implementation.

## Responsibility and dependencies

Apply deterministic defaults, profile, user, workspace, environment allowlist and explicit flags in order. Apply mandatory policy by intersection. Replace arrays atomically. Resolve and validate before activation.

First-party dependencies: [foundation](../foundation/DESIGN.md)

- [Resources](../../specifications/0300-resources/resources.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `resolve(layers, profile)`
- `migrate(raw, from_version)`

Record families: ResolvedConfig with origin per key and stable configuration digest. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ConfigLayer { source: ConfigSource, schema_major: u16, values: TypedConfig }`
- `ResolvedConfig { values, origins, policy_digest, config_digest }`

- `resolve(layers: &[ConfigLayer], mandatory: &PolicyConstraints) -> Result<ResolvedConfig>`

## Failure, safety and resource limits

Apply the resolved `configuration.max_layer_bytes` to each layer after bounded bootstrap. Reject unknown keys for version 1, duplicate keys, unavailable credential references and unsafe override attempts.

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

Permute unordered inputs and obtain identical digests. Verify a project cannot enable network against an offline policy.

## Planned source-file contracts

The entries below specify file ownership, required behavior and test cases. They are D3 drafts. Exact signature and test qualification is tracked until independent review.

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
