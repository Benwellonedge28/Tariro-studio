# Models crate design

**Contract version** 1.0. Master design §20. Planned implementation.

## Responsibility and dependencies

Resolve immutable version and license before download. Resume only under matched ETag/length or restart. Verify hash and publish atomically. Evict oldest eligible zero-pin entry.

First-party dependencies: [foundation](../foundation/DESIGN.md), [storage](../storage/DESIGN.md), [resources](../resources/DESIGN.md)

- [Model management](../../specifications/0600-model-management/model-management.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `register(manifest)`
- `import(source)`
- `resume_download(id)`
- `verify(id)`
- `evict(id)`

Record families: Manifest, content digest, checksum, source/license record, import/download checkpoint. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ModelManifest { model_id, revision, format, weights_ref, tokenizer_ref, license_id, source, capabilities, minimum_resources }`
- `TransferCursor { partial_bytes, source_validator }`

- `register(manifest: ModelManifest) -> Result<ModelRecord>`
- `verify(id: ModelId) -> Result<ModelRef>`

## Failure, safety and resource limits

No implicit network. Reject unknown license state for distribution and unsigned manifests where policy requires signatures. Preflight total bytes.

- `ChecksumMismatch`
- `LicenseRestricted`
- `DownloadChanged`
- `ModelPinned`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/models/src/
├── lib.rs
├── error.rs
├── model.rs
├── identifier.rs
├── manifest.rs
├── registry.rs
├── discovery.rs
├── download.rs
├── import.rs
├── export.rs
├── integrity.rs
├── signature.rs
├── licensing.rs
├── compatibility.rs
├── capabilities.rs
├── loader.rs
├── unloading.rs
├── cache.rs
├── lifecycle.rs
├── formats/
│   ├── mod.rs
│   ├── gguf.rs
│   ├── safetensors.rs
│   ├── onnx.rs
│   └── manifest.rs
├── tokenization/
│   ├── mod.rs
│   ├── tokenizer.rs
│   ├── vocabulary.rs
│   └── chat_template.rs
└── evaluation/
    ├── mod.rs
    ├── benchmark.rs
    ├── quality.rs
    └── performance.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Corrupt resume file, change ETag, verify only intact payload becomes Ready.
