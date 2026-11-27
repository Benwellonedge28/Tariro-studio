# Durable owner-side distributed checkpoint

**ZIP-DISTRIBUTED-CHECKPOINT-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/checkpoint.rs`

## Required implementation behavior

Record attempt, artifact/digest, progress and epoch in owner storage, rejecting stale/unverified updates. Node cache is not authority.

## Acceptance

**ZIP-DISTRIBUTED-CHECKPOINT-T01.** Worker restart cannot replace latest owner checkpoint.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
