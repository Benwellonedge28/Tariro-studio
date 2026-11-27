# Filesystem crate design

**Contract version** 1.0. Master design §40. Planned implementation.

## Responsibility and dependencies

Resolve through capability-root handles with symlink protections on every component, use same-directory temporary file and atomic replacement after condition check.

First-party dependencies: [foundation](../foundation/DESIGN.md), [security](../security/DESIGN.md)

- [Tools](../../specifications/2200-tools/tools.md)

## API and data

The operation names below define the crate boundary. Put typed requests, results and record definitions in the modules shown under Source layout. The caller supplies validated identifiers and a deadline where execution can block. Return a typed result. Accept cancellation for long operations and preserve an outcome when cancellation arrives after a durable commit.

- `open_scoped(root, path)`
- `list(root, cursor)`
- `atomic_write(target, expected_digest)`

Record families: ScopedRoot, relative path, stable file identity, snapshot operation and digest. Encode durable records versioned at the storage boundary. Use immutable digest references for payloads and revision-checked writes for mutable state. Bare integers crossing a boundary must have explicit units.

### Primary typed interface

The following contract uses Rust-shaped signatures. Names such as `Result<T>` refer to this crate's typed error result, and adapter-specific handles remain opaque to callers.

- `ScopedRoot { id, workspace_id, rights, platform_handle }`
- `WriteRequest { scoped_path, expected_digest, new_object_ref, max_bytes }`
- `WriteReceipt { digest, bytes, new_revision }`

- `atomic_write(request: WriteRequest, root: &ScopedRoot) -> Result<WriteReceipt>`

## Failure, safety and resource limits

Reject traversal, ambiguous case collisions, special device files and unsafe links on mutation. If platform proof unavailable deny untrusted writes.

- `PathOutsideScope`
- `UnsafeLink`
- `StaleFile`
- `UnsupportedIsolation`

Report the specific limiting field or missing capability and preserve safe status/evidence. A transient failure is retryable only at a documented idempotent boundary. Revalidate permissions before retries and reconcile uncertain effects before repeating writes.

## Source layout

Keep the master specification's module ownership and move a module only with an approved boundary change.

```text
crates/filesystem/src/
├── lib.rs
├── error.rs
├── path.rs
├── normalization.rs
├── canonicalization.rs
├── scope.rs
├── permissions.rs
├── reader.rs
├── writer.rs
├── atomic_write.rs
├── directory.rs
├── traversal.rs
├── watcher.rs
├── symlink.rs
├── locking.rs
├── temporary.rs
├── snapshot.rs
├── checksum.rs
└── recovery.rs
```

## Implementation and acceptance

Implement value types and validation first. Wire the successful path through its typed interface and dependency ports. Add failure and cancellation handling before promoting the feature. Then verify this crate's contract with deterministic and negative fixtures.

Test link replacement race, root escapes, concurrent CAS and failed rename rollback.
