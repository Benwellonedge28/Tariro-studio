# Intelligence routing and structured proposals

**Contract version** 1.0. Master design §71.

## Contract

The generation request carries request ID, model requirements, sensitivity, token bounds, response schema, deadline and an authorized route set. It returns chunks with strictly increasing sequence, final usage and an explicit finish reason. Text chunks are provisional until stream completion.

## Execution and integration

Route ranking is local first when compatible, followed by configured preference and stable provider/model ID. Remote routing requires a valid disclosure grant for the assembled context. Parse structured proposals once and fail schema validation with actionable error fields.

## Verification

Disconnect a stream and verify partial text is not accepted as a complete proposal. Verify offline mode never invokes a cloud provider.

Capture exact inputs, configured limits, actual result, policy revision and the evidence reference. Map applicable release requirements from [REQUIREMENTS.md](../../REQUIREMENTS.md).



## Implementing components

- [intelligence crate design](../../crates/intelligence/DESIGN.md)
- [reasoning crate design](../../crates/reasoning/DESIGN.md)
- [providers crate design](../../crates/providers/DESIGN.md)
