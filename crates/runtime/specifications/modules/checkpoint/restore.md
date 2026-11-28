# Verified checkpoint restore

**ZIP-RUNTIME-CHECKPOINT-RESTORE-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/checkpoint/restore.rs`

## Boundary and inputs

Read a pinned journal view for one approved attempt lineage and reviewed action. Walk receipts in sequence order using the verified predecessor binding and compare referenced object digest, byte count and codec edition. A successful restore returns the highest contiguous verified receipt and a bounded payload reference. An absent first checkpoint is the initial boundary. A missing, corrupt or unsupported entry within the committed prefix blocks automatic resume. Retain the preceding verified receipt for authorized diagnosis without silently rewinding.

## Behavior and failure handling

Use bounded pages and check cancellation before each page and bounded decode. Stop at the journal's recorded committed cursor. Staged objects without receipts do not enter the prefix. Checkpoint metadata may support a separately authorized successor using the same reviewed plan and action. A successor receives new authority, never the previous execution context. Restore performs no scheduler submission, resource release or external mutation.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-RESTORE-T01.** Run RT-LIFE-04 and RT-LIFE-05 in the [lifecycle fixtures](../../../../../contracts/acceptance/runtime/lifecycle-fixtures.json). Inject a missing committed object, a foreign preimage and an unsupported codec after a valid lower receipt. Preserve the lower evidence and refuse automatic resume. A cancelled read leaves the journal unchanged.
