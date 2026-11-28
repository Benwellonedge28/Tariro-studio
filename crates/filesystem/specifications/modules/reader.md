# Bounded verified reading

**ZIP-FILESYSTEM-READER-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/reader.rs`

## Boundary and inputs

Read approved regular-file bytes through an authorized scoped handle plus expected snapshot identity, optional digest and finite byte and time budgets. Verify the binding before use, stream in admitted chunks, check cancellation between chunks and reject unsupported special objects.

## Behavior and failure handling

Ranges produce range observations only. Complete receipts require exact length, expected content where provided and current identity through final verification. A partial stream or deadline cannot create a verified object receipt. Treat mutation during a snapshot read as a typed changed-state result.

## Acceptance

**ZIP-FILESYSTEM-READER-T01.** Terminate a synthetic stream early and verify no whole-file success receipt. Replace the underlying identity during read and confirm the previously checked path cannot qualify the new bytes.
