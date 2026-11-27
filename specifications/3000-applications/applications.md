# Applications and command gateway

**Contract version** 1.0. Master design §71.

## Contract

CLI, Studio, Server and Mobile are clients of one typed gateway. Every mutation carries target workspace and idempotency key or revision as applicable. Never infer approval from a UI state.

## Execution and integration

CLI exits are stable; Studio previews exact diffs and evidence; server binds loopback by default; mobile requires explicit paired access with confined review permissions. See the API and CLI documentation for wire and command details.

## Verification

Validate local CLI without editor, duplicate commands, stale approval preview and remote disabled state.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [sdk crate design](../../crates/sdk/DESIGN.md)
- [interoperability crate design](../../crates/interoperability/DESIGN.md)
