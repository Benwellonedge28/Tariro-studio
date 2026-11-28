# Checkpoint boundaries

**ZIP-RUNTIME-CHECKPOINT-MOD-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/checkpoint/mod.rs`

## Boundary and inputs

Keep checkpoint value, storage commit and restore in [checkpoint](checkpoint.md), [store](store.md) and [restore](restore.md). Expose their crate-private operations only to trusted execution and recovery code. The public Runtime façade exposes neither durable checkpoint mutation nor raw payload access. Wire the payload codec and Storage interfaces through existing Runtime dependencies.

## Behavior and failure handling

The crate boundary has no active state. A forward data path stages and verifies immutable bytes before the checkpoint transaction, then returns the committed receipt. A restart path reads and verifies the existing chain. Worker publication and recovery use their own authority checks. Dropping a wrapper or changing the codec cannot rewrite a receipt, advance the prefix or emit a second event. Module initialization performs no reads or writes.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-MOD-T01.** Compose an in-memory journal and codec. Demonstrate the same committed receipt can be consumed by the restore side, subject to its scope check. Verify a downstream crate cannot construct a private checkpoint request or replace the stored cursor directly.
