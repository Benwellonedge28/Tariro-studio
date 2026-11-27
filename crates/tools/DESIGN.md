# Tools crate design

**Contract version** 1.0. Master design §38. Planned implementation.

## Responsibility and dependencies

Resolve tool version, validate arguments and approval, reserve resources, invoke through isolated adapter, normalize and bound output, reconcile uncertain side effects.

First-party dependencies: [foundation](../foundation/DESIGN.md), [governance](../governance/DESIGN.md), [resources](../resources/DESIGN.md), [sandbox](../sandbox/DESIGN.md)

- [Tools](../../specifications/2200-tools/tools.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `register(descriptor)`
- `validate_call(input)`
- `invoke(call)`
- `reconcile(receipt)`

Record families: ToolDescriptor, typed request, capability, receipt and output artifact. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ToolDescriptor { id, version, argument_schema, effect_class, capability, output_limit }`
- `ToolReceipt { idempotency_key, status, outputs, external_receipt? }`

- `invoke(call: ToolCall, decision: AuthorizationDecision, cancel: Cancellation) -> Result<EffectOutcome<ToolReceipt>>`

## Failure, safety and resource limits

Reject arbitrary command strings or undeclared tool permissions. Deadlines and pagination mandatory. Output content cannot grant capability.

- `UnknownTool`
- `InvalidArguments`
- `CapabilityDenied`
- `AdapterTimeout`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/tools/src/
├── lib.rs
├── error.rs
├── tool.rs
├── manifest.rs
├── registry.rs
├── discovery.rs
├── invocation.rs
├── arguments.rs
├── schema.rs
├── validation.rs
├── permissions.rs
├── execution.rs
├── result.rs
├── cancellation.rs
├── timeout.rs
├── rate_limit.rs
├── auditing.rs
└── adapters/
    ├── mod.rs
    ├── native.rs
    ├── process.rs
    ├── http.rs
    ├── mcp.rs
    └── plugin.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test malformed tool calls, hallucinated tool output and unauthorized mutating calls.
