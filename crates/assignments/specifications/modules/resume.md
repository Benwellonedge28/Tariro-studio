# Explicit resume command

**ZIP-ASSIGNMENTS-RESUME-001 · v1.1 candidate · Owner** Assignments maintainers

**Planned source** `crates/assignments/src/resume.rs`

An authenticated Resume expects the current revision and a paused or recoverable assignment. Resume first moves to Recovering. Revalidate the original plan, source snapshot, applicable instructions, effective policy, evidence and currently approved grant. A cached approval, lease, worker epoch or Git reference is insufficient. An expired or revoked grant leaves prior verified units unchanged and requires a new scoped grant before dispatch. Cleanup and read-only evidence inspection use their separate scopes.

Use [recovery](recovery.md) to settle prior worker and provider obligations. Resume from the next verified unit boundary, or from verification when every unit is committed. Reach Scheduled before obtaining a fresh worker lease. If scope, required paths, source or evidence criteria changed, require explicit authority and a new plan revision. Keep historical checkpoints under their original plan. The verifier may explicitly requalify matching artifacts against the new plan and commit a contiguous prefix under its new keys. No automatic checkpoint copy.

**ZIP-ASSIGNMENTS-RESUME-T01.** An expired grant advances no unit. After a valid renewed grant for the same pinned plan, resume at the first unverified unit and retain the earlier prefix.
