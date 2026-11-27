# Durable per-node checkpoint

**ZIP-WORKFLOWS-CHECKPOINT-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/checkpoint.rs`

Key checkpoint records by workflow run, immutable plan digest and canonical node ID. Store workflow revision, node state, owner generation, stable command/job identity, accepted scheduler attempt and attempt epoch, binding and guard digests, output artifact references, trusted results and effect receipts. Persist the node transition, receipt and newly relevant readiness information through one revision-checked journal operation. Maintain deterministic eligibility as a rebuildable projection over the committed graph. Encode tagged records through the domain owner and preserve immutable evidence. A matching command replay returns its receipt. A reused command with changed inputs conflicts.

A workflow DAG may finish nodes out of order. Recover a set of valid committed node checkpoints, not a numeric contiguous cursor. Verify reachability from trusted initial inputs through declared dependencies and outcomes. Missing, corrupt or mismatched checkpoints block affected nodes. An unresolved submission or effect remains Recovering and cannot dispatch a replacement. An assignment consuming ordered units still commits its verified prefix under the separate [assignment contract](../../../../specifications/1200-assignments/assignments.md).

**ZIP-WORKFLOWS-CHECKPOINT-T01.** Commit node B before independent node A and lose its response. Restart retains B, runs eligible A, and allows the join only when both durable results exist.
