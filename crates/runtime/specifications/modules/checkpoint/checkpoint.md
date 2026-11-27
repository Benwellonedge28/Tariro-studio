# Versioned checkpoint envelope

**ZIP-RUNTIME-CHECKPOINT-CHECKPOINT-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/checkpoint/checkpoint.rs`

## Required implementation behavior

Record task, assignment, attempt epoch, monotonic sequence, plan digest, artifact digest and verification ref. No evidence-free checkpoint can advance verified progress.

## Acceptance

**ZIP-RUNTIME-CHECKPOINT-CHECKPOINT-T01.** Decode wrong version, stale epoch and mismatched digest; deny each.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
