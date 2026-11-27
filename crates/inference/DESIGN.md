# Inference crate design

**Contract version** 1.0. Master design §19. Planned implementation.

## Responsibility and dependencies

Verify weights and tokenizer, negotiate format and hardware, measure baseline and reserve, then load. Pin the handle during token generation and release on all exits.

First-party dependencies: [foundation](../foundation/DESIGN.md), [models](../models/DESIGN.md), [resources](../resources/DESIGN.md)

- [Inference](../../specifications/0500-inference/inference.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `probe()`
- `load(manifest, lease)`
- `stream(handle, request)`
- `unload(handle)`

Record families: BackendCaps, loaded model slot, generation stream and memory estimate. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `LoadRequest { manifest_digest, backend, device, lease_id }`
- `ModelHandle { backend_id, model_digest, device_id, generation }`
- `BackendCaps { formats, devices, max_context_tokens }`

- `load(request: LoadRequest, cancel: Cancellation) -> Result<ModelHandle>`

## Failure, safety and resource limits

Single generation slot on personal profile. Reject oversized context before allocation and cap output tokens. Report format or device gaps explicitly.

- `UnsupportedFormat`
- `UnsupportedDevice`
- `ContextLimit`
- `OutOfMemory`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/inference/src/
├── lib.rs
├── error.rs
├── engine.rs
├── session.rs
├── request.rs
├── response.rs
├── generation.rs
├── sampling.rs
├── streaming.rs
├── batching.rs
├── cancellation.rs
├── capabilities.rs
├── backends/
│   ├── mod.rs
│   ├── candle.rs
│   ├── mistral.rs
│   ├── ollama.rs
│   ├── llama_cpp.rs
│   ├── remote.rs
│   └── native.rs
├── hardware/
│   ├── mod.rs
│   ├── cpu.rs
│   ├── gpu.rs
│   ├── npu.rs
│   └── distributed.rs
├── memory/
│   ├── mod.rs
│   ├── allocation.rs
│   ├── kv_cache.rs
│   ├── model_cache.rs
│   └── eviction.rs
├── quantization/
│   ├── mod.rs
│   ├── formats.rs
│   ├── compatibility.rs
│   └── estimation.rs
└── metrics.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test mismatched tokenizer, bounded cancellation and controlled CPU fallback.
