# Assignment cancellation and settled outcomes

**ZIP-ASSIGNMENTS-CANCELLATION-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/cancellation.rs`

Authorize cancellation as a control action. In the transition transaction record the pending Cancel disposition, fence the worker epoch and close intake. Move to Recovering if cleanup or external effects are outstanding. Signal the supervisor outside the transaction. An effect claim linearized before cancellation may have crossed its provider boundary. An effect claim after fencing cannot start. A post-cancel worker cannot add checkpoints, emit privileged effects or overwrite observed evidence. A scoped recovery owner may record results of already-started effects.

Enter Cancelled only after runtime cleanup and all effects settle. Preserve the verified prefix and any committed provider receipt. Cancellation does not imply rollback, branch deletion or PR closure. Such actions have separate scope and intent. An unavailable cleanup verifier leaves the assignment Recovering or blocked with the stop disposition retained. Terminal replay returns the original revision and emits no new event.

**ZIP-ASSIGNMENTS-CANCELLATION-T01.** Race cancellation with provider dispatch and commit. One order prevents dispatch. The other preserves the observed outcome and does not report a terminal cancellation until cleanup and reconciliation finish.
