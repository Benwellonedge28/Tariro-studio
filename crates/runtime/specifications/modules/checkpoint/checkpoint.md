# Versioned checkpoint envelope

**ZIP-RUNTIME-CHECKPOINT-CHECKPOINT-001 · v1.1 · Owner:** Runtime maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/runtime/src/checkpoint/checkpoint.rs`

## Boundary and inputs

Checkpoint owns immutable local execution progress. Construct a candidate from the validated attempt identifier, nonzero sequence, prior checkpoint receipt digest when applicable, reviewed-plan and action digests, payload codec edition, staged object digest and verified byte length. The first sequence is one and has no prior receipt. Use Foundation identifier and digest encodings and the attempt identity from [supervisor](../supervisor.md). Validate fields without acquiring authority. The execution context supplies the current owner generation independently.

## Behavior and failure handling

Resolve the payload through Storage's immutable object interface. Check its recorded length and digest before writing a record reference. The owning codec validates the payload under admitted size and decode limits. Unknown codec editions preserve the bytes and block restore. Serialize durable metadata in the owning versioned Storage envelope. A checkpoint carries no permit, credentials, live process handle or monotonic instant. An accepted record is immutable. Repeated content alone does not identify a checkpoint across different attempts or sequences.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-CHECKPOINT-T01.** Construct the first and second checkpoint and reject a zero sequence, inconsistent predecessor, unsupported codec and mismatched staged payload length. Verify no checkpoint receipt appears on invalid input and no execution authority can be reconstructed from a checkpoint.
