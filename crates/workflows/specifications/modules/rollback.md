# Local rollback and external reconciliation

**ZIP-WORKFLOWS-ROLLBACK-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/rollback.rs`

Rollback of local state requires a verified compatible prior snapshot, current permission, a fenced writer and a separately recorded restore intent. Use the owning [storage restore boundary](../../../storage/specifications/modules/backup/restore.md) via composition. Verify the restored state and preserve all authoritative external effect evidence under the recovery journal. An unavailable target, incompatible schema or uncertain selector blocks further dispatch pending recovery.

External effects remain durable even if local state was restored. Resolve them through original effect reconciliation or explicitly authorized [compensation](compensation.md). Do not infer absence from a rewound journal. Preserve per-effect outcomes, actual rollback evidence and unresolved work. Never mark a run restored merely because rollback was requested.

**ZIP-WORKFLOWS-ROLLBACK-T01.** A local restore preserves the prior external receipt and cannot regenerate an already confirmed operation. Incompatible writer schema blocks activation.
