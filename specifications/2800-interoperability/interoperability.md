# Protocol interoperability

**Contract version** 1.0. Master design §71.

## Contract

Public protocol envelopes carry major/minor version, request ID, actor context and size limits. Separate transport errors from typed operation outcomes. Normalize capability versions and reject unknown required fields.

## Execution and integration

Map local IPC, HTTPS/SSE, authenticated worker RPC, MCP, LSP, DAP and Wasm through negotiated adapters. Never widen scope during translation. Optional ULABI activates only after conformance.

## Verification

Cross-version golden request/response pairs, disconnect/resume, limit errors and unsupported capabilities.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [interoperability crate design](../../crates/interoperability/DESIGN.md)
- [sdk crate design](../../crates/sdk/DESIGN.md)
- [providers crate design](../../crates/providers/DESIGN.md)
