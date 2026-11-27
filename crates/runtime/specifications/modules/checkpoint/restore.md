# Verified checkpoint restore

**ZIP-RUNTIME-CHECKPOINT-RESTORE-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/checkpoint/restore.rs`

## Required implementation behavior

Read highest contiguous checkpoint for pinned plan, verify digests, lease epoch and current authority. Missing content or incompatible serialization blocks resume with reason.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-RESTORE-T01.** Corrupt latest checkpoint does not silently infer success or advance cursor.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
