# Verified resumable artifact exchange

**ZIP-DISTRIBUTED-ARTIFACT-TRANSFER-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/artifact_transfer.rs`

## Required implementation behavior

Require exact digest, lengths, allowed class/destination and admitted bytes, stage chunks and verify completion before activation.

## Acceptance

**ZIP-DISTRIBUTED-ARTIFACT-TRANSFER-T01.** Interrupted resume cannot partially promote artifact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
