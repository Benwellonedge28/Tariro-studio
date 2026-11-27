# Restart and external-effect recovery

**ZIP-RCV-001 · v1.0 · Owner:** Runtime and repository maintainers. **Maturity:** D4 candidate.

Startup validates storage version and integrity before accepting writes. Recreate only recoverable work from the highest contiguous verified checkpoint. Fence prior worker epochs. Revalidate grant, policy, deadline and artifact digests before resuming.

For each external effect record a stable effect key, expected external state, reviewed payload digest, reconciliation function and current outcome before dispatch. An uncertain outcome invokes read-only reconciliation using narrow authority. If the target exactly matches, record receipt. If absence is proven and the grant and preconditions remain valid, allow a retry within budget. An ambiguous or conflicting target blocks. Never retry an unknown mutation blindly.

Report corruption, incompatibility and revoked scope separately. Resume never invents completion or silently widens an effect. Fault-injection tests simulate interrupted local commit, lost push/PR acknowledgment and expired grant during recovery.
